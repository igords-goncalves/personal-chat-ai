from langchain_community.document_loaders import YoutubeLoader


def yt_loader(url: str):
    loader = YoutubeLoader.from_youtube_url(youtube_url=url, language=["pt"])
    document_list = loader.load()
    # print(document_list[0].page_content) --> debuug

    yt_info = ""
    for info in document_list:
        yt_info += info.page_content

    return yt_info
    