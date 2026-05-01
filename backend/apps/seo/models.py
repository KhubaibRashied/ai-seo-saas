class SEOCampaign:
    def __init__(self, keyword, target_url, status):
        self.keyword = keyword
        self.target_url = target_url
        self.status = status

    def __repr__(self):
        return f"SEOCampaign(keyword={self.keyword}, target_url={self.target_url}, status={self.status})"