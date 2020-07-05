from bs4 import BeautifulSoup
import csv
import re

def getSoup(flname):
    with open(flname, "r", encoding="utf8") as fl:
        soup_obj = BeautifulSoup(fl, features="html.parser")

    return soup_obj


def TagLabel():
    """
    Tag标签：
        * .name: 获取tag的名字
        * .attrs: 获取tag的属性
        * .string: 获取tag中包含的字符串
    """
    soup_obj = getSoup("getop.html")
    tag = soup_obj.p

    print("tag(soup_obj.p):\n", tag)
    print("\ntype(tag):\n", type(tag))
    print("\ntag.name:\n", tag.name)
    print("\ntag.attrs:\n", tag.attrs)
    print("\ntag.string:\n", tag.string.strip())


def ChildrenNode():
    """
    子节点：
        * .children: 子节点的生成器，可以对tag的子节点进行循环
        * .contents: 将子节点以列表方式返回
        * .descendants: 将字符串也作为子节点返回
        * .strings: 将该节点及其子节点中的所有字符串都找出来
        * .stripped_strings: 将该节点及其子结点中除了空格和空行的所有字符串都找出来
    """
    soup_obj = getSoup("getop.html")
    tag = soup_obj.head

    print("tag(soup_obj.head):\n", tag)
    print("\ntag.children:\n", tag.children)
    print("\ntag.contents:\n", tag.contents)
    print("\ntag.contents等价写法:\n", [i for i in tag.children])   # 这一句等价于tag.contents
    print("\ntag.descendants:\n", [i for i in tag.descendants])
    print("\ntag.strings:\n", [i for i in tag.strings])
    print("\ntag.stripped_strings:\n", [i for i in tag.stripped_strings])


def ParentNode():
    """
    父节点：
        * .parent: 获取某个元素的父节点
        * .parents: 获取某个元素的全部父节点
    """
    soup_obj = getSoup("ParentNode.html")
    tag = soup_obj.a

    print("tag(soup_obj.link):\n", tag)
    print("\ntag.parent:\n", tag.parent)
    print("\ntag.parent.name:\n", tag.parent.name)
    print("\ntag.parents:\n", [i for i in tag.parents])
    print("\ntag.parents(name):\n", [i.name for i in tag.parents])


def BrotherNode():
    """
    兄弟节点：
        * .next_sibling: 该节点的后一个兄弟节点
        * .previous_sibling: 该节点的前一个兄弟节点
        * .next_siblings: 该节点之后的全部兄弟节点
        * .previous_siblings: 该节点之前的全部兄弟节点
    """
    soup_obj = getSoup("BrotherNode.html")
    tag = soup_obj.e

    print("tag(soup_obj.e):\n", tag)
    print("\ntag.next_sibling:\n", tag.next_sibling)
    print("\ntag.previous_sibling:\n", tag.previous_sibling)
    print("\ntag.next_siblings:\n", [i for i in tag.next_siblings])
    print("\ntag.next_siblings(name):\n", [i.name for i in tag.next_siblings])
    print("\ntag.previous_sibling:\n", [i for i in tag.previous_siblings])
    print("\ntag.previous_sibling(name):\n", [i.name for i in tag.previous_siblings])


def BackandForword():
    """
    前进和后退：
        * .next_element: 该元素的后一个元素
        * .previous_element: 该元素的前一个元素
        * .next_elements: 该元素后面的全部元素
        * .previous_elements: 该元素前面的全部元素
    """
    soup_obj = getSoup("BrotherNode.html")
    tag = soup_obj.e

    print("tag(soup_obj.e):\n", tag)
    print("\ntag.next_element:\n", tag.next_element)
    print("\ntag.previous_element:\n", tag.previous_element)
    print("\ntag.next_elements:\n", [i for i in tag.next_elements])
    print("\ntag.next_elements(name):\n", [i.name for i in tag.next_elements])
    print("\ntag.previous_elements:\n", [i for i in tag.previous_elements])
    print("\ntag.previous_elements(name):\n", [i.name for i in tag.previous_elements])


def selectFun(tag):
    # print("\ntag的debug:\n", tag.attrs)
    return tag.has_attr("class") and tag.attrs["class"] == ["nowrap"]


def cssSelect(css_class):
    return css_class is not None and len(css_class) == 6


def find_allFun():
    """
    find_all方法：
        * name参数：查找所有名字为name的tag，字符串对象会自动被忽略掉
        * keyword参数：搜索时会把该参数当作指定名字tag的属性来搜索
        * text参数：通过text参数可以搜索文档中的字符串内容
        * limit参数：限制返回结果的数量
        * recursive参数：如果只想搜索tag的直接子节点，可以使用参数recursive=False
    """
    soup_obj = getSoup("ParentNode.html")
    tag = soup_obj.body

    # name参数
    print("tag(soup_obj.body):\n", tag)
    print("\ntag.find_all(\"p\"):\n", tag.find_all("p"))                                          # name参数为字符串
    print("\ntag.find_all(re.compile(\"[ap]\")):\n", tag.find_all(re.compile("[ap]")))            # name参数为正则表达式
    print("\ntag.find_all([\"a\", \"p\"]):\n", tag.find_all(["a", "p"]))                          # name参数为列表
    print("\ntag.find_all(True):\n", [i.name for i in tag.find_all(True)])                        # name参数为True
    print("\ntag.find_all(selectFun):\n", tag.find_all(selectFun))                                # name参数为函数

    # keyword参数
    print("\ntag.find_all(class_=\"alert alert-info\"):\n", tag.find_all(class_="alert alert-info"))
    print("\ntag.find_all(class_=re.compile(\"info\")):\n", tag.find_all(class_=re.compile("info")))
    print("\ntag.find_all(class_=cssSelect):\n", tag.find_all(class_=cssSelect))
    print("\ntag.find_all(\"p\", attrs={\"class\": [\"alert\", \"alert-info\"]}):\n", tag.find_all("p", attrs={"class": ["alert", "alert-info"]}))
    print("\ntag.find_all(\"p\", attrs={\"class\": [\"alert\", \"alert-info\", \"nowrap\"]}):\n", tag.find_all("p", attrs={"class": ["alert", "alert-info", "nowrap"]}))

    # text参数: 与上面的name参数一样，text参数也可以接收字符串，正则表达式，列表，True。
    print("\ntag.find_all(text=\"Latest Outputs\")\n", tag.find_all(text=" Latest Outputs "))

    # limit参数
    print("\ntag.find_all(\"p\", limit=1)\n", tag.find_all("p", limit=1))

    # recursive参数
    print("\ntag.find_all(\"a\", recursive=False)\n", tag.find_all("a", recursive=False))


def selectData():
    soup_obj = getSoup("get_using_cookie.html")

    for attr_tr in soup_obj.find_all("tbody", id="tbl_main"):
        print([attr_th.text.strip() for attr_th in attr_tr.find_all("th")])

    for attr_tr in soup_obj.find_all("tr", class_=re.compile(r"[eo]")):
        print([attr_td.text.strip() for attr_td in attr_tr.find_all("td")])


if __name__ == "__main__":
    # selectData()
    # TagLabel()
    # ChildrenNode()
    # ParentNode()
    # BrotherNode()
    # BackandForword()
    find_allFun()