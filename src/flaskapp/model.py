from transformers import pipeline


summarizer = pipeline(task='summarization')


def get_summary(long_text, max_length):
    summary = summarizer(
        long_text,
        max_length=max_length
    )

    summary_text = summary[0]['summary_text']

    return summary_text


## During testing
# def get_summary(long_text, max_length):
# 	return long_text[:max_length]
