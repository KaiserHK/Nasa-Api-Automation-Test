import pytest
from test_requests import make_request

class TestClass:
    
    def test_SearchWithSuccess(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        
        #Act
        response = make_request(key);
        
        #Assert
        assert response.status_code == 200;
        data = response.json();
        assert len(data) > 0;
        assert data["element_count"] > 0;
        
    def test_SearchWithoutQueryParameters(self):
        #Arrange
        query = "";
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 403;

    def test_SearchWithStartDateOnly(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        startDate = "start_date=2023-01-01";
        query = startDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        
    def test_SearchWithEndDateOnly(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        endDate = "end_date=2000-01-01";
        query = endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        
    def test_SearchWithValidDateRange(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        startDate = "start_date=2022-01-01";
        endDate = "end_date=2023-01-01";
        query = startDate + "&" + endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        
    def test_SearchWithInvalidDateRange(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        startDate = "start_date=2000-01-01";
        endDate = "end_date=1999-01-01";
        query = startDate + "&" + endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 400;
        
    def test_SearchWithInvalidApiToken(self):
        #Arrange
        key = "api_key=SOME_TOKEN";
        
        #Act
        response = make_request(key);
        
        #Assert
        assert response.status_code == 403;
