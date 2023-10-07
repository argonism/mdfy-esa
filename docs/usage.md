# Usage

To use mdfy-esa in a project

```python
import mdfy_esa
rom mdfy import MdImage, MdLink, MdText
from mdfy_esa import EsaMdfier
contents = [
    MdText("This is a test article."),
    MdImage(src="example/test_image.png"),
    MdLink(url="example/dummy.pdf"),
]
mdfier = EsaMdfier(post_fullname="note/me/My Test Article", esa_team="test_team")
mdfier.write(contents=contents)
```
