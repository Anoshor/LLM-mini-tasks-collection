from bing_image_downloader import downloader

search_terms = [
    "bag", "pen", "laptop", "phone", "bed", "vehicle",
    "chair", "table", "book", "watch"
]

for term in search_terms:
    downloader.download(term, limit=200, output_dir='dataset', 
                        adult_filter_off=True, force_replace=False, timeout=60)
