from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


SYNTAX_ERROR_FIELD_MAP = {
    '1stFlrSF': 'FirstFlrSF',
    '2ndFlrSF': 'SecondFlrSF',
    '3SsnPorch': 'ThreeSsnPortch'
}

class CANCER_DATASET(Schema):
    radius_mean = fields.Float()
    texture_mean = fields.Float()
    perimeter_mean = fields.Float()
    area_mean = fields.Float()
    smoothness_mean = fields.Float()
    compactness_mean = fields.Float()
    concavity_mean = fields.Float()
    concave_points_mean = fields.Float()
    symmetry_mean = fields.Float()
    fractal_dimension_mean = fields.Float()
    radius_se = fields.Float()
    texture_se = fields.Float()
    perimeter_se = fields.Float()
    area_se = fields.Float()
    smoothness_se = fields.Float()
    compactness_se = fields.Float()
    concavity_se = fields.Float()
    concave_points_se = fields.Float()
    symmetry_se = fields.Float()
    fractal_dimension_se = fields.Float()
    radius_worst = fields.Float()
    texture_worst = fields.Float()
    perimeter_worst = fields.Float()
    area_worst = fields.Float()
    smoothness_worst = fields.Float()
    compactness_worst = fields.Float()
    concavity_worst = fields.Float()
    concave_points_worst = fields.Float()
    symmetry_worst = fields.Float()
    fractal_dimension_worst = fields.Float()



def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = CANCER_DATASET()

    final_dict = {}
    for i, j in input_data.items():
        final_dict[i.replace(" ", "_")] = j

    input_data = final_dict
    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages
    print(input_data)
    # convert syntax error field names back
    # this is a hack - never name your data
    # fields with numbers as the first letter.
    # for dict in input_data:
    #     for key, value in SYNTAX_ERROR_FIELD_MAP.items():
    #         dict[key] = dict[value]
    #         del dict[value]

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data
    print('raj',[validated_input])
    return [validated_input], errors

