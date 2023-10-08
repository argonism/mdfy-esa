import os
from typing import Any, Dict

from mdfy import MdImage, MdLink, MdText

from mdfy_esa import EsaMdfier


def create_post(post_fullname: str, esa_team: str) -> Dict[str, Any]:
    contents = [
        MdText("This is a test article."),
        MdImage(src="examples/test_image.png"),
        MdLink(url="examples/dummy.pdf"),
    ]

    mdfier = EsaMdfier(post_fullname=post_fullname, esa_team=esa_team)
    return mdfier.write(contents=contents)


def update_post(post_number: int, esa_team: str) -> Dict[str, Any]:
    contents = [
        MdText("This is a test article."),
        MdText("This is a test article."),
        MdImage(src="examples/test_image.png"),
        MdLink(url="examples/dummy.pdf"),
    ]

    mdfier = EsaMdfier(post_number=post_number, esa_team=esa_team)
    return mdfier.write(contents=contents)


if __name__ == "__main__":
    post_fullname = "note/me/My Test Article"
    esa_team = os.environ["ESA_TEAM"]
    created_post = create_post(post_fullname, esa_team)
    updated_post = update_post(created_post["number"], esa_team)
    print("post updated!:", updated_post["url"])
