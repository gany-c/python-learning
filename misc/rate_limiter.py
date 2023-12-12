"""
In Python, write code for a Rate limiter -

Each customer can make X requests per Y seconds;
Assuming that customer ID is extracted somehow from the request, Perform rate
limiting logic for provided customer ID.

implement the following function

Return true if the request is allowed, and false if it is not.
def rateLimit(customerId: int ) -> bool:
"""

class RateLimiter:
    """
    Create a dict
    key = Customer_id
    Value = queue of size X_rea
    """

    def __init__(self, X_req, Y_sec):
        self.X_req  = X_req
        self.Y_sec = Y_sec

    def __is_request_allowed(self, customer_id):
        """
        1. get queue based on customer_id
        2. if size lesser than X_req, add now_ts to queue, return true
        3. else, examine the first item of queue, if it is lesser than Y_sec return false
        4. else, pop the item and do 2.
        :param customer_id:
        :return:
        """
        pass

    def your_api_call(self, request):
        """
        customer_id = request.customer_id

        if not self.__is_request_allowed(customer_id):
            return false
        :param request:
        :return:
        """

        # What if the service is load balanced?
        # Easiest is to divide X_req by num_instances
        # Or else store the state in a DB or Remote server
        # LB design https://www.geeksforgeeks.org/how-to-design-a-rate-limiter-api-learn-system-design/
