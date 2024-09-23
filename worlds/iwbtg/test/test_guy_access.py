from . import MyGameTestBase


class TestGuyAccess(MyGameTestBase):
    options = {
        "guy_open": ["Orbs"],
        "additional_progression_items": ["Link"],
    }

    def test_guy_access(self) -> None:
        """Test locations that require a sword"""
        locations = ["Guy Defeated"]
        items = [["Link"]]
        # This tests that the provided locations aren't accessible without the provided items, but can be accessed once
        # the items are obtained.
        # This will also check that any locations not provided don't have the same dependency requirement.
        # Optionally, passing only_check_listed=True to the method will only check the locations provided.
        self.assertAccessDependency(locations, items)