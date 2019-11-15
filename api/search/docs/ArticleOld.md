# ArticleOld

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**id** | **str** | Article identifier | 
**title** | **str** | Article title | 
**description** | **str** | Short description | 
**main_body** | **str** | Main contents of the article in html format. | 
**video_url** | **str** | If the article has a video, contains absolute url of this video.  | [optional] 
**url** | **str** | K-ruoka.fi url of this article. | [optional] 
**last_modified** | **str** | Date when this article was last modified. | [optional] 
**visible_from** | **str** | Date when the article is made visible on the website. | 
**visible_to** | **str** | Date when the article is unpublished. | 
**images** | [**ArticleOldImages**](ArticleOldImages.md) |  | [optional] 
**categories** | [**list[ArticleOldCategories]**](ArticleOldCategories.md) | Associated categories. | 
**sort** | **list[float]** | Only present, if the results are sorted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


