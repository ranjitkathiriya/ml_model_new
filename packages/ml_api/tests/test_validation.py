import json

from regression_model.config import config as model_config
from regression_model.processing.data_management import load_dataset


def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the regression_model package.
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    post_json = test_data.drop(['Unnamed: 0','id','diagnosis'],axis=1).to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/classfication',
                                      json=json.loads(post_json))

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    #
    # # Check correct number of errors removed
    assert len(response_json.get('predictions')), len(test_data)
