from langchain_community.document_loaders import YoutubeLoader


def yt_loader(url: str):
    loader = YoutubeLoader.from_youtube_url(url, language=["pt"])
    information = loader.load()
    # print(document_list[0].page_content) --> debuug

    yt_infos = ""
    for info in information:
        yt_infos += info.page_content

    return yt_infos
