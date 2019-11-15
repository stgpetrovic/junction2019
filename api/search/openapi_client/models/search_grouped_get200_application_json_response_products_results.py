# coding: utf-8

"""
    Search API

    Search API is a REST-like API which wraps the underlying ElasticSearch service for most common use cases. While this API is called the \"search\" service, in practice it acts as the main data engine for various Kesko services, providing high performance endpoints for fetching recipe, product, offer, store and article data.    API requests are only served over HTTPS, using TLS 1.0, 1.1, and 1.2. Requests will not be honored over plaintext HTTP.    Use of `accept: application/json` and `content-type: application/json` headers is required when applicable.    The API uses UTF-8 character encoding for all responses. Some fields may include characters that are not in the ASCII range.    As every other Kesko API service in this hackathon, authentication is accomplished by providing `Ocp-Apim-Subscription-Key` header with your subscription key as the value.    Submitting excessive requests to the server may result in a HTTP 429 Too Many Requests status code and temporary limitations to your Subscription. We kindly ask that you to limit the concurrency of your requests and/or insert 50 – 100 milliseconds of delay between the requests you send to the server. (i.e., 10 requests per second on average), since this environment doesn't run with the same specs as the real production instance.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SearchGroupedGet200ApplicationJsonResponseProductsResults(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'resource_type': 'str',
        'data_source': 'str',
        'ean': 'str',
        'ean_replaced': 'str',
        'ean_replacing': 'str',
        'url_slug': 'str',
        'label_name': 'ProductLabelName',
        'marketing_name': 'ProductLabelName',
        'description': 'ProductLabelName',
        'measurements': 'ProductMeasurements',
        'segment': 'ProductLabelName',
        'category': 'ProductLabelName',
        'subcategory': 'ProductLabelName',
        'is_consumer_good': 'bool',
        'brand': 'str',
        'attributes': 'dict(str, ProductAttributes)',
        'picture_urls': 'ProductPictureUrls',
        'ingredient_type': 'ProductIngredientType',
        'pricing_unit': 'str',
        'popularity': 'float',
        'is_alcohol': 'bool'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'data_source': 'dataSource',
        'ean': 'ean',
        'ean_replaced': 'eanReplaced',
        'ean_replacing': 'eanReplacing',
        'url_slug': 'urlSlug',
        'label_name': 'labelName',
        'marketing_name': 'marketingName',
        'description': 'description',
        'measurements': 'measurements',
        'segment': 'segment',
        'category': 'category',
        'subcategory': 'subcategory',
        'is_consumer_good': 'isConsumerGood',
        'brand': 'brand',
        'attributes': 'attributes',
        'picture_urls': 'pictureUrls',
        'ingredient_type': 'ingredientType',
        'pricing_unit': 'pricingUnit',
        'popularity': 'popularity',
        'is_alcohol': 'isAlcohol'
    }

    def __init__(self, resource_type=None, data_source=None, ean=None, ean_replaced=None, ean_replacing=None, url_slug=None, label_name=None, marketing_name=None, description=None, measurements=None, segment=None, category=None, subcategory=None, is_consumer_good=None, brand=None, attributes=None, picture_urls=None, ingredient_type=None, pricing_unit=None, popularity=None, is_alcohol=None, local_vars_configuration=None):  # noqa: E501
        """SearchGroupedGet200ApplicationJsonResponseProductsResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resource_type = None
        self._data_source = None
        self._ean = None
        self._ean_replaced = None
        self._ean_replacing = None
        self._url_slug = None
        self._label_name = None
        self._marketing_name = None
        self._description = None
        self._measurements = None
        self._segment = None
        self._category = None
        self._subcategory = None
        self._is_consumer_good = None
        self._brand = None
        self._attributes = None
        self._picture_urls = None
        self._ingredient_type = None
        self._pricing_unit = None
        self._popularity = None
        self._is_alcohol = None
        self.discriminator = None

        self.resource_type = resource_type
        self.data_source = data_source
        self.ean = ean
        self.ean_replaced = ean_replaced
        self.ean_replacing = ean_replacing
        self.url_slug = url_slug
        if label_name is not None:
            self.label_name = label_name
        if marketing_name is not None:
            self.marketing_name = marketing_name
        if description is not None:
            self.description = description
        if measurements is not None:
            self.measurements = measurements
        if segment is not None:
            self.segment = segment
        if category is not None:
            self.category = category
        if subcategory is not None:
            self.subcategory = subcategory
        if is_consumer_good is not None:
            self.is_consumer_good = is_consumer_good
        if brand is not None:
            self.brand = brand
        self.attributes = attributes
        self.picture_urls = picture_urls
        if ingredient_type is not None:
            self.ingredient_type = ingredient_type
        if pricing_unit is not None:
            self.pricing_unit = pricing_unit
        if popularity is not None:
            self.popularity = popularity
        self.is_alcohol = is_alcohol

    @property
    def resource_type(self):
        """Gets the resource_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The resource_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param resource_type: The resource_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["product"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and resource_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def data_source(self):
        """Gets the data_source of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        Indicates the source of the product data. `kRuoka` for Tuotetietopankki products, store ID for local products. <br>For hackathon purposes, you should be able to safely ignore this field.   # noqa: E501

        :return: The data_source of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        Indicates the source of the product data. `kRuoka` for Tuotetietopankki products, store ID for local products. <br>For hackathon purposes, you should be able to safely ignore this field.   # noqa: E501

        :param data_source: The data_source of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_source is None:  # noqa: E501
            raise ValueError("Invalid value for `data_source`, must not be `None`")  # noqa: E501

        self._data_source = data_source

    @property
    def ean(self):
        """Gets the ean of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        EAN13 number. Length is always 13. When necessary, the number has been padded with leading zeros.   # noqa: E501

        :return: The ean of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        EAN13 number. Length is always 13. When necessary, the number has been padded with leading zeros.   # noqa: E501

        :param ean: The ean of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ean is None:  # noqa: E501
            raise ValueError("Invalid value for `ean`, must not be `None`")  # noqa: E501

        self._ean = ean

    @property
    def ean_replaced(self):
        """Gets the ean_replaced of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        EAN13 number. `eanReplaced` has been replaced by `ean`. Length is always 13. When necessary, the number has been padded with leading zeros.   # noqa: E501

        :return: The ean_replaced of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._ean_replaced

    @ean_replaced.setter
    def ean_replaced(self, ean_replaced):
        """Sets the ean_replaced of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        EAN13 number. `eanReplaced` has been replaced by `ean`. Length is always 13. When necessary, the number has been padded with leading zeros.   # noqa: E501

        :param ean_replaced: The ean_replaced of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ean_replaced is None:  # noqa: E501
            raise ValueError("Invalid value for `ean_replaced`, must not be `None`")  # noqa: E501

        self._ean_replaced = ean_replaced

    @property
    def ean_replacing(self):
        """Gets the ean_replacing of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        EAN13 number. `eanReplacing` will replace `ean`. Length is always 13. When necessary, the number has been padded with leading zeros.   # noqa: E501

        :return: The ean_replacing of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._ean_replacing

    @ean_replacing.setter
    def ean_replacing(self, ean_replacing):
        """Sets the ean_replacing of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        EAN13 number. `eanReplacing` will replace `ean`. Length is always 13. When necessary, the number has been padded with leading zeros.   # noqa: E501

        :param ean_replacing: The ean_replacing of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ean_replacing is None:  # noqa: E501
            raise ValueError("Invalid value for `ean_replacing`, must not be `None`")  # noqa: E501

        self._ean_replacing = ean_replacing

    @property
    def url_slug(self):
        """Gets the url_slug of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        Product url slug  # noqa: E501

        :return: The url_slug of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._url_slug

    @url_slug.setter
    def url_slug(self, url_slug):
        """Sets the url_slug of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        Product url slug  # noqa: E501

        :param url_slug: The url_slug of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `url_slug`, must not be `None`")  # noqa: E501

        self._url_slug = url_slug

    @property
    def label_name(self):
        """Gets the label_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The label_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductLabelName
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param label_name: The label_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductLabelName
        """

        self._label_name = label_name

    @property
    def marketing_name(self):
        """Gets the marketing_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The marketing_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductLabelName
        """
        return self._marketing_name

    @marketing_name.setter
    def marketing_name(self, marketing_name):
        """Sets the marketing_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param marketing_name: The marketing_name of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductLabelName
        """

        self._marketing_name = marketing_name

    @property
    def description(self):
        """Gets the description of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The description of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductLabelName
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param description: The description of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductLabelName
        """

        self._description = description

    @property
    def measurements(self):
        """Gets the measurements of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The measurements of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductMeasurements
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        """Sets the measurements of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param measurements: The measurements of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductMeasurements
        """

        self._measurements = measurements

    @property
    def segment(self):
        """Gets the segment of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The segment of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductLabelName
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param segment: The segment of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductLabelName
        """

        self._segment = segment

    @property
    def category(self):
        """Gets the category of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The category of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductLabelName
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param category: The category of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductLabelName
        """

        self._category = category

    @property
    def subcategory(self):
        """Gets the subcategory of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The subcategory of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductLabelName
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param subcategory: The subcategory of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductLabelName
        """

        self._subcategory = subcategory

    @property
    def is_consumer_good(self):
        """Gets the is_consumer_good of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        Is the product a consumer good (true) or a foodstuff (false).   # noqa: E501

        :return: The is_consumer_good of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: bool
        """
        return self._is_consumer_good

    @is_consumer_good.setter
    def is_consumer_good(self, is_consumer_good):
        """Sets the is_consumer_good of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        Is the product a consumer good (true) or a foodstuff (false).   # noqa: E501

        :param is_consumer_good: The is_consumer_good of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: bool
        """

        self._is_consumer_good = is_consumer_good

    @property
    def brand(self):
        """Gets the brand of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        `pirkka`, `kmenu` or undefined   # noqa: E501

        :return: The brand of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        `pirkka`, `kmenu` or undefined   # noqa: E501

        :param brand: The brand of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        allowed_values = ["pirkka", "kmenu"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and brand not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `brand` ({0}), must be one of {1}"  # noqa: E501
                .format(brand, allowed_values)
            )

        self._brand = brand

    @property
    def attributes(self):
        """Gets the attributes of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        A JSON object representing all possible attributes, that have been defined for a product. Every key in the object maps to product database attribute names. <br>In this interface, a value of a key is either an attribute object or an array of attribute objects. Here you can find the list of possible attributes. Attributes with their name ending with '?' might be missing from the responses, and this data might sometimes contain surprises. <br> EAN11: EAN code<br> MATKL: Product category number<br> PRODUCT_DESCRIPTION?: Product description<br> MAKTX?: Name, Finnish<br> MAKTXEN?: Name, English<br> MAKTXRU?: Name, Swedish<br> MAKTM_U?: Marketing name, Finnish<br> MAKTM_E?: Marketing name, English<br> MAKTM_V?: Marketing name, Swedish<br> MAKTE?: Some name field??<br> PDB_BLOCKING_CODE?: Blocking code<br> PDB_BLOCKING_CODE_DATE?: Blocking code effective date<br> ZZBRAND?: Brand<br> ZZSAISO?: Seasonality<br> ZZVENDOR?: Manufacturer<br> KUPAEAN11?: Transport unit EAN (like the EAN of whole box of sweets)<br> KUVPAI?: Product activity flag<br> LIFNR?: SAP vendor account number<br> INHAL?: Net contents<br> INHME?: Content unit<br> NTGEW?: Net weight<br> KAYMAA?: ????<br> KAYMAY?: ????<br> UMRE?: ????<br> STRAS?: Street address<br> PSTLZ?: Postal code<br> ORT01?: Name of city<br> LOCALITY_OF_MANUFACTURE?: Locality of manufacture<br> LAND1?: Country code<br> LANDX?: Country code in Finnish<br> MANUFA?: Country of manufacturer<br> WHERL?: Country of origin<br> INPP_U?: Recipe, Finnish<br> INPP_E?: Recipe, English<br> INPP_V?: Recipe, Swedish<br> MATERIAL_U?: Product ingredients description, Finnish<br> MATERIAL_E?: Product ingredients description, English<br> MATERIAL_V?: Product ingredients description, Swedish<br> TX_ADD_U?: Additive property, Finnish<br> TX_ADD_E?: Additive property, English<br> TX_ADD_V?: Additive property, Swedish<br> TX_CONT?: List of ingredients<br> TX_ERIOMI?: Special properties for non-food items<br> TX_KIEOMI?: Recycling emblems<br> TX_PAKMER?: Packaging emblems<br> TX_RAVOMI?: Nutritional properties<br> TX_YMPMER?: Responsibility emblems<br> LAST_CHANGE_DATE?: Change date<br> SYNDICATION_APPROVAL_DATE?: Approval date<br> ZZDISCODATE?: Product removed from market date<br> ZZENDDA?: New product release date<br> CAUTIONARY_INSTRUCTIONS?: Cautionary notes<br> HEATING_PREPARATION_INSTRUCTIONS?: Heating and preparation instructions<br> STORAGE_INSTRUCTIONS?: Storage instructions<br> USAGE_INSTRUCTIONS?: Usage instructions<br> ZCONUSE?: Storage and operating instructions<br> ALKPI?: Alcohol content %<br> AVITAM?: Vitamin A (µg)<br> B12VIT?: Vitamin B12 (µg)<br> B6VITA?: Vitamin B6 (mg)<br> BIOTII?: Biotin (µg)<br> CVITAM?: Vitamin C (mg)<br> DVITAM?: Vitamin D (µg)<br> EVITAM?: Vitamin E (µg)<br> ENERKC?: Energy content kcal/100g<br> ENERKJ?: Energy content kJ/100g<br> FLUORI?: Fluorine (mg)<br> FOOLIH?: Folic acid (µg)<br> FOSFOR?: Phosphorus (mg)<br> HIHYDR?: Carbohydrates / 100g<br> HIHYSO?: Polyol (g)<br> HIHYTA?: Starch (g)<br> JODI?: Iodine (µg)<br> KALIUM?: Potassium (mg)<br> KALSIU?: Calcium (mg)<br> KLORID?: Chloride (mg)<br> KOSTPI?: Moisture content %<br> KROMI?: Chrome (µg)<br> KUPARI?: Copper (mg)<br> KUIVPI?: Dry matter content %<br> KUITUA?: Nutritional fiber / 100g<br> KVITAM?: Vitamin K (µg)<br> LAKTOO?: Lactose / 100g<br> LIHAPI?: Meat/fish content %<br> MAGNES?: Magnesium (mg)<br> MANGAA?: Manganese (mg)<br> MAITPI?: Milk fat content %<br> MARJPI?: Berry- or fruit content %<br> MELAIS?: Dilution ratio % <br> MOLYB?: Molybdenum<br> NATPIT?: Sodium (g)<br> NIASIN?: Niacin (mg)<br> PANTOT?: Pantothenic acid (mg)<br> PROTEG?: Protein / 100g<br> RAAPAI?: Quantity of raw materials / 100g<br> RASKTY?: Monounsaturated (g)<br> RASMTY?: Polyunsaturated (g)<br> RASVAA?: Fat / 100g<br> RASVPI?: Fat content %<br> RAUTAA?: Iron (mg)<br> RAVITAM?: Vitamin A RDA<br> RB12VIT?: Vitamin B12 RDA<br> RB6VITA?: Vitamin B6 RDA<br> RBIOTII?: Biotin RDA<br> RCVITAM?: Vitamin C RDA<br> RDVITAM?: Vitamin D RDA<br> REVITAM?: Vitamin E RDA<br> RFLUORI?: Fluorine RDA<br> RFOOLIH?: Folic acid RDA<br> RFOSFOR?: Phosphorus RDA<br> RIBOFL?: Riboflavin (mg)<br> RJODI?: Iodine RDA<br> RKALIUM?: Potassium RDA<br> RKALSIU?: Calcium RDA<br> RKLORID?: Chloride RDA<br> RKROMI?: Chrome RDA<br> RKUPARI?: Copper RDA<br> RKVITAM?: Vitamin K RDA<br> RMAGNES?: Magnesium RDA<br> RMANGAA?: Manganese RDA<br> RMOLYB?: Molybdenum RDA<br> RNATPIT?: Sodium RDA<br> RNIASIN?: Niacin RDA<br> RPANTOT?: Pantothenic acid RDA<br> RRAUTAA?: Iron RDA<br> RRIBOFL?: Riboflavin RDA<br> RSELEEN?: Selenium RDA<br> RSINKKI?: Zinc RDA<br> RTIAMII?: Thiamine RDA<br> SELEEN?: Selenium (µg<br> SINKKI?: Zinc (mg)<br> SOKEPI?: Sugar content %<br> SOKERI?: Sugars / 100g<br> SUKLPI?: Cocoa content %<br> SUOLA?: Salt (g)<br> SUOLPI?: Salinity %<br> TAMEPI?: Juice content %<br> TIAMII?: Thiamine (mg)<br> TYYDPI?: Unsaturated fats %<br> TYYDRH?: Saturated fat / 100g<br> TAR_HIHYDR?: Measurement precision: carbohydrates<br> TAR_HIHYSO?: Measurement precision: polyol<br> TAR_HIHYTA?: Measurement precision: starch<br> TAR_KUITUA?: Measurement precision: nutritional fiber<br> TAR_LAKTOO?: Measurement precision: lactose<br> TAR_PROTEG?: Measurement precision: protein<br> TAR_RASKTY?: Measurement precision: monounsaturated<br> TAR_RASMTY?: Measurement precision: polyunsaturated<br> TAR_RASVAA?: Measurement precision: fat<br> TAR_SOKERI?: Measurement precision: sugars<br> TAR_SUOLA?: Measurement precision: salt<br> TAR_TYYDRH?: Measurement precision: saturated fat<br>   # noqa: E501

        :return: The attributes of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: dict(str, ProductAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        A JSON object representing all possible attributes, that have been defined for a product. Every key in the object maps to product database attribute names. <br>In this interface, a value of a key is either an attribute object or an array of attribute objects. Here you can find the list of possible attributes. Attributes with their name ending with '?' might be missing from the responses, and this data might sometimes contain surprises. <br> EAN11: EAN code<br> MATKL: Product category number<br> PRODUCT_DESCRIPTION?: Product description<br> MAKTX?: Name, Finnish<br> MAKTXEN?: Name, English<br> MAKTXRU?: Name, Swedish<br> MAKTM_U?: Marketing name, Finnish<br> MAKTM_E?: Marketing name, English<br> MAKTM_V?: Marketing name, Swedish<br> MAKTE?: Some name field??<br> PDB_BLOCKING_CODE?: Blocking code<br> PDB_BLOCKING_CODE_DATE?: Blocking code effective date<br> ZZBRAND?: Brand<br> ZZSAISO?: Seasonality<br> ZZVENDOR?: Manufacturer<br> KUPAEAN11?: Transport unit EAN (like the EAN of whole box of sweets)<br> KUVPAI?: Product activity flag<br> LIFNR?: SAP vendor account number<br> INHAL?: Net contents<br> INHME?: Content unit<br> NTGEW?: Net weight<br> KAYMAA?: ????<br> KAYMAY?: ????<br> UMRE?: ????<br> STRAS?: Street address<br> PSTLZ?: Postal code<br> ORT01?: Name of city<br> LOCALITY_OF_MANUFACTURE?: Locality of manufacture<br> LAND1?: Country code<br> LANDX?: Country code in Finnish<br> MANUFA?: Country of manufacturer<br> WHERL?: Country of origin<br> INPP_U?: Recipe, Finnish<br> INPP_E?: Recipe, English<br> INPP_V?: Recipe, Swedish<br> MATERIAL_U?: Product ingredients description, Finnish<br> MATERIAL_E?: Product ingredients description, English<br> MATERIAL_V?: Product ingredients description, Swedish<br> TX_ADD_U?: Additive property, Finnish<br> TX_ADD_E?: Additive property, English<br> TX_ADD_V?: Additive property, Swedish<br> TX_CONT?: List of ingredients<br> TX_ERIOMI?: Special properties for non-food items<br> TX_KIEOMI?: Recycling emblems<br> TX_PAKMER?: Packaging emblems<br> TX_RAVOMI?: Nutritional properties<br> TX_YMPMER?: Responsibility emblems<br> LAST_CHANGE_DATE?: Change date<br> SYNDICATION_APPROVAL_DATE?: Approval date<br> ZZDISCODATE?: Product removed from market date<br> ZZENDDA?: New product release date<br> CAUTIONARY_INSTRUCTIONS?: Cautionary notes<br> HEATING_PREPARATION_INSTRUCTIONS?: Heating and preparation instructions<br> STORAGE_INSTRUCTIONS?: Storage instructions<br> USAGE_INSTRUCTIONS?: Usage instructions<br> ZCONUSE?: Storage and operating instructions<br> ALKPI?: Alcohol content %<br> AVITAM?: Vitamin A (µg)<br> B12VIT?: Vitamin B12 (µg)<br> B6VITA?: Vitamin B6 (mg)<br> BIOTII?: Biotin (µg)<br> CVITAM?: Vitamin C (mg)<br> DVITAM?: Vitamin D (µg)<br> EVITAM?: Vitamin E (µg)<br> ENERKC?: Energy content kcal/100g<br> ENERKJ?: Energy content kJ/100g<br> FLUORI?: Fluorine (mg)<br> FOOLIH?: Folic acid (µg)<br> FOSFOR?: Phosphorus (mg)<br> HIHYDR?: Carbohydrates / 100g<br> HIHYSO?: Polyol (g)<br> HIHYTA?: Starch (g)<br> JODI?: Iodine (µg)<br> KALIUM?: Potassium (mg)<br> KALSIU?: Calcium (mg)<br> KLORID?: Chloride (mg)<br> KOSTPI?: Moisture content %<br> KROMI?: Chrome (µg)<br> KUPARI?: Copper (mg)<br> KUIVPI?: Dry matter content %<br> KUITUA?: Nutritional fiber / 100g<br> KVITAM?: Vitamin K (µg)<br> LAKTOO?: Lactose / 100g<br> LIHAPI?: Meat/fish content %<br> MAGNES?: Magnesium (mg)<br> MANGAA?: Manganese (mg)<br> MAITPI?: Milk fat content %<br> MARJPI?: Berry- or fruit content %<br> MELAIS?: Dilution ratio % <br> MOLYB?: Molybdenum<br> NATPIT?: Sodium (g)<br> NIASIN?: Niacin (mg)<br> PANTOT?: Pantothenic acid (mg)<br> PROTEG?: Protein / 100g<br> RAAPAI?: Quantity of raw materials / 100g<br> RASKTY?: Monounsaturated (g)<br> RASMTY?: Polyunsaturated (g)<br> RASVAA?: Fat / 100g<br> RASVPI?: Fat content %<br> RAUTAA?: Iron (mg)<br> RAVITAM?: Vitamin A RDA<br> RB12VIT?: Vitamin B12 RDA<br> RB6VITA?: Vitamin B6 RDA<br> RBIOTII?: Biotin RDA<br> RCVITAM?: Vitamin C RDA<br> RDVITAM?: Vitamin D RDA<br> REVITAM?: Vitamin E RDA<br> RFLUORI?: Fluorine RDA<br> RFOOLIH?: Folic acid RDA<br> RFOSFOR?: Phosphorus RDA<br> RIBOFL?: Riboflavin (mg)<br> RJODI?: Iodine RDA<br> RKALIUM?: Potassium RDA<br> RKALSIU?: Calcium RDA<br> RKLORID?: Chloride RDA<br> RKROMI?: Chrome RDA<br> RKUPARI?: Copper RDA<br> RKVITAM?: Vitamin K RDA<br> RMAGNES?: Magnesium RDA<br> RMANGAA?: Manganese RDA<br> RMOLYB?: Molybdenum RDA<br> RNATPIT?: Sodium RDA<br> RNIASIN?: Niacin RDA<br> RPANTOT?: Pantothenic acid RDA<br> RRAUTAA?: Iron RDA<br> RRIBOFL?: Riboflavin RDA<br> RSELEEN?: Selenium RDA<br> RSINKKI?: Zinc RDA<br> RTIAMII?: Thiamine RDA<br> SELEEN?: Selenium (µg<br> SINKKI?: Zinc (mg)<br> SOKEPI?: Sugar content %<br> SOKERI?: Sugars / 100g<br> SUKLPI?: Cocoa content %<br> SUOLA?: Salt (g)<br> SUOLPI?: Salinity %<br> TAMEPI?: Juice content %<br> TIAMII?: Thiamine (mg)<br> TYYDPI?: Unsaturated fats %<br> TYYDRH?: Saturated fat / 100g<br> TAR_HIHYDR?: Measurement precision: carbohydrates<br> TAR_HIHYSO?: Measurement precision: polyol<br> TAR_HIHYTA?: Measurement precision: starch<br> TAR_KUITUA?: Measurement precision: nutritional fiber<br> TAR_LAKTOO?: Measurement precision: lactose<br> TAR_PROTEG?: Measurement precision: protein<br> TAR_RASKTY?: Measurement precision: monounsaturated<br> TAR_RASMTY?: Measurement precision: polyunsaturated<br> TAR_RASVAA?: Measurement precision: fat<br> TAR_SOKERI?: Measurement precision: sugars<br> TAR_SUOLA?: Measurement precision: salt<br> TAR_TYYDRH?: Measurement precision: saturated fat<br>   # noqa: E501

        :param attributes: The attributes of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: dict(str, ProductAttributes)
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def picture_urls(self):
        """Gets the picture_urls of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The picture_urls of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductPictureUrls
        """
        return self._picture_urls

    @picture_urls.setter
    def picture_urls(self, picture_urls):
        """Sets the picture_urls of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param picture_urls: The picture_urls of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductPictureUrls
        """
        if self.local_vars_configuration.client_side_validation and picture_urls is None:  # noqa: E501
            raise ValueError("Invalid value for `picture_urls`, must not be `None`")  # noqa: E501

        self._picture_urls = picture_urls

    @property
    def ingredient_type(self):
        """Gets the ingredient_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The ingredient_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: ProductIngredientType
        """
        return self._ingredient_type

    @ingredient_type.setter
    def ingredient_type(self, ingredient_type):
        """Sets the ingredient_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param ingredient_type: The ingredient_type of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: ProductIngredientType
        """

        self._ingredient_type = ingredient_type

    @property
    def pricing_unit(self):
        """Gets the pricing_unit of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501


        :return: The pricing_unit of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: str
        """
        return self._pricing_unit

    @pricing_unit.setter
    def pricing_unit(self, pricing_unit):
        """Sets the pricing_unit of this SearchGroupedGet200ApplicationJsonResponseProductsResults.


        :param pricing_unit: The pricing_unit of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: str
        """
        allowed_values = ["kpl", "kg"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pricing_unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pricing_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(pricing_unit, allowed_values)
            )

        self._pricing_unit = pricing_unit

    @property
    def popularity(self):
        """Gets the popularity of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        Popularity index, popular products have bigger number   # noqa: E501

        :return: The popularity of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: float
        """
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        """Sets the popularity of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        Popularity index, popular products have bigger number   # noqa: E501

        :param popularity: The popularity of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: float
        """

        self._popularity = popularity

    @property
    def is_alcohol(self):
        """Gets the is_alcohol of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501

        Indicates whether the product is considered alcohol or not. Determined by comparing product segment to OMS alcohol blacklist segment listing.   # noqa: E501

        :return: The is_alcohol of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :rtype: bool
        """
        return self._is_alcohol

    @is_alcohol.setter
    def is_alcohol(self, is_alcohol):
        """Sets the is_alcohol of this SearchGroupedGet200ApplicationJsonResponseProductsResults.

        Indicates whether the product is considered alcohol or not. Determined by comparing product segment to OMS alcohol blacklist segment listing.   # noqa: E501

        :param is_alcohol: The is_alcohol of this SearchGroupedGet200ApplicationJsonResponseProductsResults.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_alcohol is None:  # noqa: E501
            raise ValueError("Invalid value for `is_alcohol`, must not be `None`")  # noqa: E501

        self._is_alcohol = is_alcohol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchGroupedGet200ApplicationJsonResponseProductsResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchGroupedGet200ApplicationJsonResponseProductsResults):
            return True

        return self.to_dict() != other.to_dict()
