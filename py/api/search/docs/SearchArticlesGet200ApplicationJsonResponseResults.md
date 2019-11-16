# SearchArticlesGet200ApplicationJsonResponseResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**id** | **str** | Article identifier | 
**legacy_id** | **int** | Episerver article identifier | [optional] 
**title** | **str** | Article title | 
**description** | **str** | Short description | 
**ingress** | **str** | Ingress of the article. | [optional] 
**body** | **str** | Main contents of the article in markdown format. | [optional] 
**header_image_url** | **str** | If the article has a header image, contains the absolute url of this image.  | [optional] 
**header_video_url** | **str** | If the article has a header video, contains the absolute url of this video.  | [optional] 
**original_url** | **str** | K-ruoka.fi url of this article. | [optional] 
**created_at** | **str** | Date when this article was created. | 
**updated_at** | **str** | Date when this article was last modified. | 
**categories** | [**list[ArticleCategories]**](ArticleCategories.md) | Associated categories. | 
**slug** | **str** | URL slug of the article | 
**theme_slug** | **str** | URL slug of the article theme | [optional] 
**sort** | **list[float]** | Only present, if the results are sorted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


