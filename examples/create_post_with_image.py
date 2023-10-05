import os

from mdfy import MdImage, MdLink, MdText

from mdfy_esa import EsaMdfier


def main(post_fullname: str, esa_team: str) -> None:
    contents = [
        MdText("This is a test article."),
        MdImage(src="examples/test_image.png"),
        MdLink(url="examples/dummy.pdf"),
    ]

    mdfier = EsaMdfier(post_fullname=post_fullname, esa_team=esa_team)
    mdfier.write(contents=contents)


if __name__ == "__main__":
    post_fullname = "ノート/k-ush/2023/実験メモ_2023-10-04"
    esa_team = os.environ["ESA_TEAM"]
    main(post_fullname, esa_team)
