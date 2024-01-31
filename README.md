**When migrations don't work remove all the migrations**

```
find . -path "_/migrations/_.py" -not -name "**init**.py" -delete
```

**Responses also go through middlewares like the CSRF and other common middlewares.**

This is how we initializer the JWT auth for the django

```
REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}
```

## AbstractUser vs AbstractBaseUser

abstractUser is for less customization but AbstractBaseUser is for entire modification.

# steps each request follows:

1. dispatch -->first method called on entering view; handles content negotiation and method dispatching.

2. http_method_not_allowed --> validates the view's method with incoming http_method (block if GET instead of POST sen)

3. initial --> setup needed for the view

4. check_permissions --> checks whether requesting user has necessary permissions

5. check_throttles --> checks if request should be throttled.

6. post:

   1. main method for handling POST request.

   2. serializer=TaskSerializer(data=data): -->creates an instance of TaskSerializer with incoming data

   3. serializer.is_valid() --> calls the is_valid():
      a. serializer.run_validation -->trigerring validation for each field individually.

      b. to_internal_value(data) --> method on each field to convert raw input data to valid internal representation

      c. validate\_<field_name>(value)-->validate individual field

      d. validate(value) --> calls the validate method of serializer which can be overridden in serializer to perform additional validation across multiple fields.

   4. serializer.save() --> if data is valid this method internally calls the CREATE method

   5. to_representation() --> after the object is saved, then this method converts in a form that is ready to send the data.

7. finalize_response -->called after the main HTTP method handler. responsible for finalizing the response object.

8. handle_exception --> handles any exceptions raised during the processing of the request.

first create the instance
then with the is*valid()
run different validations:
run_validation
to_internal_value(data)
validate<field_name>
validate

1. dispatch
2. http_method_not_allowed
3. initial -->setup
4. permissions -->check permissions
5. throttles --> rate limiting
6. serializer obj instanciation
7. is_valid() called and run_validation()
    8. to_internal_value()
    9. validate_<field_name>
    10. validate -->validate 2 object
    11. to_representation method
12. finalize response
13. handle_exception -->to handle any exception
