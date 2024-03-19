# Basic Ride Sharing API with Class-Based Viewsets

## User API

Implement API endpoints for user registration and login using Django Rest Framework (DRF).

## Ride API

- Create a Django model for Rides with fields: rider, driver, pickup_location, dropoff_location, status, created_at, updated_at.
- Implement API endpoints for creating a ride request, viewing a ride's details, and listing all rides.

## Ride Status Updates

- Implement API endpoints for updating the status of a ride. For example, when a ride is started, completed, or cancelled.

## Real-time Ride Tracking (***Bonus for Juniors***)

- Implement a simulation of real-time ride tracking. This could involve periodically updating the ride's current location.

## Bonus I (***Bonus for Juniors***)

### Ride Matching

- Implement an algorithm for matching ride requests with available drivers. This could be based on proximity, or other factors.
- Implement an API endpoint for drivers to accept a ride request.

## Bonus II (***Bonus for Juniors***)

- Write basic Django tests for the models and API endpoints. 

### Advanced Testing (***Bonus for Seniors***)

  - Write tests for the ride matching algorithm, the ride status updates, the driver API endpoints, and the ride tracking simulation.