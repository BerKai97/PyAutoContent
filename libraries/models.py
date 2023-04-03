from typing import Optional, List
from sqlmodel import (Field, SQLModel, Relationship, ForeignKey, MetaData)

PublicMeta = MetaData()

class Content(SQLModel, table=True):
    __tablename__ = "Content"
    metadata = PublicMeta
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(nullable=False, index=True)
    description: str = Field(nullable=True, index=False)
    content: str = Field(nullable=False, index=False)
    tags: List[str] = Field(default_factory=list)
    category: int = Field(foreign_key="ContentCategory.id", nullable=False, index=True)
    topic: int = Field(foreign_key="", nullable=False, index=False)
    # relationships
    category_rel: Optional["ContentCategory"] = Relationship(back_populates="content_rel")
    topic_rel: Optional["ContentTopic"] = Relationship(back_populates="content_rel")
    playlist_rel: Optional["Playlist"] = Relationship(back_populates="content_rel")

class Playlist(SQLModel, table=True):
    __tablename__ = "Playlist"
    metadata = PublicMeta
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(nullable=False, index=True)
    description: str = Field(nullable=True, index=False)
    # relationships
    contents : List["Content"] = Relationship(back_populates="playlist_rel")

class ContentCategory(SQLModel, table=True):
    __tablename__ = "ContentCategory"
    metadata = PublicMeta
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(nullable=False, index=True)
    # relationships
    contents : List["Content"] = Relationship(back_populates="category_rel")

class ContentTopic(SQLModel, table=True):
    __tablename__ = "ContentTopic"
    metadata = PublicMeta
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(nullable=False, index=True)
    top_topic: int = Field(foreign_key="ContentTopic.id", nullable=True, index=True)
    # relationships
    contents : List["Content"] = Relationship(back_populates="topic_rel")