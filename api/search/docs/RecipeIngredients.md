# RecipeIngredients

Represents a single part of the recipe such as \"Sauce\", \"Frosting\" or \"Additionally\". The main part of the recipe generally does not have a heading, in which case the sub section heading value is underscore (`\"_\"`). <br>Ingredients can have alternatives in recipes. For example, you could have \"lemon juice OR orange juice\". In recipe data, alternative ingredients are listed in an Array. If an ingredient does not have alternatives, the Array only has one ingredient. SubSectionIngredients is an Array of ingredient alternatives, i.e. it is an Array of Array of Ingredient Objects. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_section_heading** | **str** | Name of the sub section. | 
**sub_section_ingredients** | **list[list[object]]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


