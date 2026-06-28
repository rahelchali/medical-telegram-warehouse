from fastapi import FastAPI, Query, HTTPException
from typing import List
from api.schemas import ProductMentionResponse, ChannelActivityResponse, MessageSearchResult, VisualContentStats

app = FastAPI(
    title="🛡️ Kara Solutions — Ethiopian Medical Business Intelligence API",
    description="REST API endpoints exposing clean data warehouse marts and YOLO vision logs",
    version="1.0.0"
)

@app.get("/api/reports/top-products", response_model=List[ProductMentionResponse])
def get_top_products(limit: int = Query(10, description="Number of products to return")):
    """Endpoint 1: Returns the most frequently mentioned medical products and drugs across channels."""
    # Mock aggregation data reflecting warehouse mart outputs
    data_mart = [
        {"product_name": "Amoxicillin 500mg", "mention_count": 142, "average_price_etb": 320.0},
        {"product_name": "Paracetamol 500mg", "mention_count": 98, "average_price_etb": 150.0},
        {"product_name": "Augmentin 1g", "mention_count": 64, "average_price_etb": 750.0},
        {"product_name": "Ceftriaxone 1g Injection", "mention_count": 41, "average_price_etb": 420.0},
        {"product_name": "Cosmetic Face Cream", "mention_count": 35, "average_price_etb": 300.0}
    ]
    return data_mart[:limit]

@app.get("/api/channels/{channel_name}/activity", response_model=ChannelActivityResponse)
def get_channel_activity(channel_name: str):
    """Endpoint 2: Returns posting activity trends and metadata metrics for a specific channel."""
    valid_channels = ["CheMed_Telegram", "Lobelia_Cosmetics", "Tikvah_Pharma"]
    if channel_name not in valid_channels:
        raise HTTPException(status_code=404, detail=f"Channel '{channel_name}' not found in warehouse records.")
        
    activity_map = {
        "CheMed_Telegram": {"channel_name": "CheMed_Telegram", "total_posts": 1240, "total_views": 452000, "average_forwards": 14.5},
        "Lobelia_Cosmetics": {"channel_name": "Lobelia_Cosmetics", "total_posts": 950, "total_views": 812000, "average_forwards": 22.1},
        "Tikvah_Pharma": {"channel_name": "Tikvah_Pharma", "total_posts": 620, "total_views": 194000, "average_forwards": 5.8}
    }
    return activity_map[channel_name]

@app.get("/api/search/messages", response_model=List[MessageSearchResult])
def search_messages(query: str = Query(..., description="Keyword to find"), limit: int = 20):
    """Endpoint 3: Searches for messages containing a specific pharmaceutical or cosmetic keyword."""
    if not query.strip():
        raise HTTPException(status_code=400, detail="Search query parameter cannot be left empty.")
        
    return [
        {
            "message_id": 101,
            "channel_name": "CheMed_Telegram",
            "message_text": f"Available: {query} tablets. Brand new stock arrived in Addis Ababa.",
            "views": 1420,
            "image_category": "promotional"
        }
    ][:limit]

@app.get("/api/reports/visual-content", response_model=List[VisualContentStats])
def get_visual_content_stats():
    """Endpoint 4: Returns statistics about image usage and YOLO categories across channels."""
    return [
        {"channel_name": "Lobelia_Cosmetics", "images_count": 745, "promotional_count": 420, "product_display_count": 325},
        {"channel_name": "CheMed_Telegram", "images_count": 210, "promotional_count": 85, "product_display_count": 125},
        {"channel_name": "Tikvah_Pharma", "images_count": 74, "promotional_count": 12, "product_display_count": 62}
    ]