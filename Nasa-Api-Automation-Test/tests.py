import pytest
from test_requests import make_request

class TestClass:
    
    def SearchWithSuccess():
        #Arrange
        #Act
        #Assert
        pass;
    def SearchWithoutQueryParameters():
        #Arrange
        #Act
        #Assert
        pass;
    def SearchWithStartDateOnly():
        #Arrange
        #Act
        #Assert
        pass;
    def SearchWithEndDateOnly():
        #Arrange
        #Act
        #Assert
        pass;
    def SearchWithValidDateRange():
        #Arrange
        #Act
        #Assert
        pass;
    def SearchWithInvalidDateRange():
        #Arrange
        #Act
        #Assert
        pass;
    def SearchWithInvalidApiToken():
        #Arrange
        #Act
        #Assert
        pass;



def test_search_asteroids_with_success():
    #Arrange
    api = "api_key=DEMO_KEY"

    #Act
    response = make_request(api)

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data["element_count"] > 0
    print(data)


