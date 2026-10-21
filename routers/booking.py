from fastapi import APIRouter, HTTPException, status, Depends

from exceptions import booking_exceptions
from exceptions import show_exceptions

from models.requests.bookings.create_booking import CreateBookingRequest
from models.requests.bookings.fetch_booking import FetchBookingRequest
from models.requests.bookings.cancel_booking import CancelBookingRequest

from models.domain.bookings.booking import Booking
from models.domain.payments.payment import Payment

from models.database.bookings.booking_status import BookingStatus
from models.database.payments.payment_status import PaymentStatus

from models.response.bookings.create_booking import CreateBookingResponse
from models.response.bookings.fetch_booking import FetchBookingResponse
from models.response.bookings.cancel_booking import CancelBookingResponse

import utils.getId as getId 
from datetime import datetime, timezone

from service.booking import BookingService
from dependency import create_booking_service

def createBookingRouter():
    router = APIRouter()

    @router.post("/createBooking")
    async def create_booking(booking_to_create_body:CreateBookingRequest, bookingService:BookingService = Depends(create_booking_service)):

        payment = Payment(id = getId.getRandomId(),
                          amount = booking_to_create_body.payment_details.amount,
                          mode = booking_to_create_body.payment_details.mode,
                          status= PaymentStatus.PENDING)
        
        new_booking = Booking(id = getId.getRandomId(), 
                        user_id = booking_to_create_body.user_id, 
                        status = BookingStatus.PENDING,
                        payment_id= payment.id,
                        seat_ids = booking_to_create_body.seat_ids, 
                        show_id = booking_to_create_body.show_id, 
                        requested_time = datetime.now(timezone.utc),
                        booking_time = datetime.now(timezone.utc)
                        )

        try:
            created_booking = bookingService.createBooking(new_booking, payment)
            created_booking_response = CreateBookingResponse.model_validate(created_booking)
            return {"Created Booking" : created_booking_response}

        except booking_exceptions.BookingAlreadyExists as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail=str(e)
            )

    @router.post("/fetchBooking")
    async def fetch_booking(booking_to_fetch_body:FetchBookingRequest, bookingService:BookingService = Depends(create_booking_service)):

        try:
            fetched_booking = bookingService.fetchBooking(booking_to_fetch_body)
            fetched_booking_response = FetchBookingResponse.model_validate(fetched_booking)
            return {"Fetched Booking" : fetched_booking_response}

        except booking_exceptions.BookingNotFoundException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            )

    @router.put("/cancelBooking")
    async def cancel_booking(booking_to_cancel_body:CancelBookingRequest,bookingService:BookingService = Depends(create_booking_service)):

        try:
            cancelled_booking = bookingService.cancelBooking(booking_to_cancel_body)
            cancelled_booking_response = CancelBookingResponse.model_validate(cancelled_booking)
            return {"Cancelled Booking" : cancelled_booking_response}

        except booking_exceptions.BookingNotFoundException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=str(e)
            ) 

    return router