import pytest;
from test_requests import make_request;
import datetime;

class TestClass:

    def test_SearchWithoutQueryParameters(self):
        #Arrange
        query = "";
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 403;

    def test_SearchWithInvalidApiToken(self):
        #Arrange
        key = "api_key=SOME_TOKEN";
        
        #Act
        response = make_request(key);
        
        #Assert
        assert response.status_code == 403;
    
    def test_SearchWithNoDates(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        
        #Act
        response = make_request(key);
        
        #Assert
        assert response.status_code == 200;
        data = response.json();
        assert len(data) > 0;
        assert data["element_count"] > 0;

    def test_SearchWithStartDateOnly(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        startDate = "start_date=2023-01-01";
        query = startDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        data = response.json();
        assert len(data) > 0;
        assert data["element_count"] > 0;
        
    def test_SearchWithEndDateOnly(self):
        #Arrange
        today = datetime.datetime.now();
        sevenDaysAgo = today - datetime.timedelta(days = 7);
        
        key = "api_key=DEMO_KEY";
        endDate = "end_date=" + sevenDaysAgo.strftime('%Y-%m-%d');
        query = endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        data = response.json();
        assert len(data) > 0;
        assert data["element_count"] > 0;
        
    def test_SearchWithValidDateRange(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        startDate = "start_date=2022-01-01";
        endDate = "end_date=2022-01-08";
        query = startDate + "&" + endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        data = response.json();
        assert len(data) > 0;
        assert data["element_count"] > 0;
        
    def test_SearchWithStartDateAfterEndDate(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        startDate = "start_date=2023-01-08";
        endDate = "end_date=2023-01-01";
        query = startDate + "&" + endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 200;
        data = response.json();
        assert len(data) > 0;
        assert data["element_count"] > 0;

    def test_SearchWithDateRangeOfEightDays(self):
        #Arrange
        today = datetime.datetime.now();
        eightDaysAgo = today - datetime.timedelta(days = 8);
        
        key = "api_key=DEMO_KEY";
        endDate = "end_date=" + eightDaysAgo.strftime('%Y-%m-%d');
        query = endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 400;

    def test_SearchWithInvalidDateFormat(self):
        #Arrange
        today = datetime.datetime.now();
        
        key = "api_key=DEMO_KEY";
        endDate = "end_date=" + today.strftime('%m-%d-%Y');
        query = endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 400;

    def test_SearchWithCharactersInDates(self):
        #Arrange
        key = "api_key=DEMO_KEY";
        endDate = "end_date=YYYY-MM-DD";
        query = endDate + "&" + key;
        
        #Act
        response = make_request(query);
        
        #Assert
        assert response.status_code == 400;
