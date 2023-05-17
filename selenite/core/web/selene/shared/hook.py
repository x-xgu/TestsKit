import allure


def attach_video_on_failure(video_src: str) -> None:
    """
    Attach video on test failure.

    Args:
        video_src (str): The source of the video.

    Returns:
        None.

    Example:
        >>> attach_video_on_failure('https://example.com/video.mp4')
    """
    body = f"""
    <video 
        controls="" 
        style="max-width: auto; height: 100%;" 
        src="{video_src}" 
        alt="">
        
    </video>
    """
    allure.attach(
        body=body,
        name='video',
        attachment_type=allure.attachment_type.HTML
    )
