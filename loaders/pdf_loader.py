from langchain_community.document_loaders import PyPDFLoader


def pdf_loader(path: str):
    loader = PyPDFLoader(file_path=path)
    document_list = loader.load()

    pdf_info = ""
    for info in document_list:
        pdf_info += info.page_content

    return pdf_info
