"""Tests for the current get_user(user_id) contract."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from profileapp.cli import main
from profileapp.roster import team_roster
from profileapp.directory import UnknownUser, get_user


class GetUserContractTests(unittest.TestCase):
    def test_known_id_returns_the_directory_record(self):
        user = get_user(1)
        self.assertEqual(user["name"], "Alice Chen")
        self.assertEqual(user["email"], "alice.chen@example.com")
        self.assertEqual(user["team"], "Engineering")
        self.assertEqual(user["title"], "Backend engineer")

    def test_missing_id_raises_unknown_user(self):
        with self.assertRaises(UnknownUser):
            get_user(99)

    def test_team_roster_looks_up_each_member(self):
        members = team_roster("Engineering")
        self.assertEqual([member["id"] for member in members], [1, 3])

    def test_show_command_prints_the_profile(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["show", "--id", "1"])
        self.assertEqual(code, 0)
        self.assertIn("Loads user Alice Chen (ID 1)", stdout.getvalue())

    def test_show_command_rejects_an_unknown_id(self):
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = main(["show", "--id", "99"])
        self.assertEqual(code, 1)
        self.assertIn("No user with id 99", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
