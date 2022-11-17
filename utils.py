from typing import List


def get_infos(logfile_path: str) -> List[str]:
    """Search for a "info" in a file and returns the corresponding paragraph
     Args:
        logfile_path: The path of log file to be used to search for "info"
    Returns:
        The list of paragraphs that contain "INFO"   
    """
    return get_paragraphs_contain_keyword(
        file_path=logfile_path,
        keyword="INFO"
    )


def get_errors(logfile_path: str) -> List[str]:
    """Search for a "error" in a file and returns the corresponding paragraph
     Args:
        logfile_path: The path of log file to be used to search for "error"
    Returns:
        The list of paragraphs that contain "ERROR"   
    """
    return get_paragraphs_contain_keyword(
        file_path=logfile_path,
        keyword="ERROR"
    )


def get_warnings(logfile_path: str) -> List[str]:
    """Search for a "warning" in a file and returns the corresponding paragraph
     Args:
        logfile_path: The path of log file to be used to search for the keyword
    Returns:
        The list of paragraphs that contain "WARNING"   
    """
    return get_paragraphs_contain_keyword(
        file_path=logfile_path,
        keyword="WARNING"
    )


def get_paragraphs_contain_keyword(file_path: str, keyword: str) -> List[str]:
    """Search for a specific keyword in a file and returns the corresponding paragraphs
    
    Args:
        file_path: The path of the file to be used to search for the keyword
        keyword: The keyword to be look for in the file
    Returns:
        The list of paragraphs that correspond to the keyword
    """
    all_paragraphs = []

    with open(file=file_path, mode="r") as thefile:
        file_content = thefile.read()
        all_paragraphs = file_content.split('\n')

    paragraphs_contain_keyword = []
    for paragraph in all_paragraphs:
        if keyword in paragraph:
            paragraphs_contain_keyword.append(paragraph)
    
    return paragraphs_contain_keyword