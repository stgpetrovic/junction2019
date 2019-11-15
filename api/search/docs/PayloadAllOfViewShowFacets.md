# PayloadAllOfViewShowFacets

A boolean value, or an object determining if faceting should be enabled. `true` means that default facet info is included, `false` means that facet info is not included. <br>Default value is `false`. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facets** | **list[str]** | A string or an array of strings that determines which facets should be included in the response. Dot separated facets like &#x60;categories.id&#x60; can be matched with just a part of the full value like &#x60;categories&#x60;. All facets are returned by default.  | [optional] 
**limit** | **int** | Defines how many categories should be returned. Categories with most hits are prioritized. &lt;br&gt;Default value is 250.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


