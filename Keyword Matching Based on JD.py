def keyword_match(resume_text, job_desc):
    resume_words = set(resume_text.lower().split())
    jd_words = set(job_desc.lower().split())
    common = resume_words.intersection(jd_words)
    return common
