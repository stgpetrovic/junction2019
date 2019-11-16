# SearchGroupedGet200ApplicationJsonResponseRecipesResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**id** | **str** | Recipe identifier | 
**name** | **str** | Recipe name | 
**url** | **str** | Recipe url in k-ruoka.fi | 
**url_slug** | **str** | Recipe url slug | 
**piece_size** | [**RecipePieceSize**](RecipePieceSize.md) |  | [optional] 
**portion_cost** | **str** | Cost per portion in Euros | 
**portions** | [**RecipePortions**](RecipePortions.md) |  | [optional] 
**preparation_time** | [**RecipePreparationTime**](RecipePreparationTime.md) |  | [optional] 
**categories** | [**list[RecipeCategories]**](RecipeCategories.md) |  | 
**pictures** | **list[str]** | Array of recipe picture ids | [optional] 
**picture_urls** | [**list[RecipePictureUrls]**](RecipePictureUrls.md) |  | [optional] 
**video_url** | **str** |  | 
**video_embed_url** | **str** |  | 
**trend_words** | [**list[RecipeTrendWords]**](RecipeTrendWords.md) |  | 
**special_diets** | [**list[RecipeSpecialDiets]**](RecipeSpecialDiets.md) |  | 
**energy_amounts** | [**RecipeEnergyAmounts**](RecipeEnergyAmounts.md) |  | 
**ingredients** | [**list[RecipeIngredients]**](RecipeIngredients.md) |  | 
**instructions** | **str** | Preparation instructions | 
**end_note** | **str** | Short note about the recipe | 
**description** | **str** | Recipe description | 
**date_created** | **date** | Creation date and time | [optional] 
**tv_date** | **date** | Mitä tänään syötäisiin TV date | [optional] 
**date_modified** | **date** | Modification date and time | [optional] 
**recipe_use** | [**RecipeRecipeUse**](RecipeRecipeUse.md) |  | [optional] 
**stamp** | [**RecipeStamp**](RecipeStamp.md) |  | [optional] 
**sort** | **list[float]** | Recipe search results are always sorted primarily based on relevance score. Secondary sorting parameter is the id of the recipe, largest id first. Id sorting tries to return newest recipes first. Sort array contains information about search parametes, first index is the relevance score, second the Id of the recipe.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


