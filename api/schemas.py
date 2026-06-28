from pydantic import BaseModel
from typing import List, Optional

class ProductMentionResponse(BaseModel):
    product_name: str
    mention_count: int
    average_price_etb: float

class ChannelActivityResponse(BaseModel):
    channel_name: str
    total_posts: int
    total_views: int
    average_forwards: float

class MessageSearchResult(BaseModel):
    message_id: int
    channel_name: str
    message_text: str
    views: int
    image_category: Optional[str] = None

class VisualContentStats(BaseModel):
    channel_name: str
    images_count: int
    promotional_count: int
    product_display_count: int