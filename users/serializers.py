import qrcode
from io import BytesIO
import base64
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'rank', 'security_clearance', 'qr_code']
        read_only_fields = ['qr_code']

    def create(self, validated_data):
        # Extract the data needed for generating the QR code
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        rank = validated_data['rank']
        security_clearance = validated_data['security_clearance']

        # Generate the content for the QR code
        qr_content = f"Email: {email}\nName: {first_name} {last_name}\nRank: {rank}\nSecurity Clearance: {security_clearance}"

        # Generate the QR code image
        qr = qrcode.make(qr_content)

        # Save the QR code image to a BytesIO buffer
        buffer = BytesIO()
        qr.save(buffer, format='PNG')

        # Encode the QR code image to base64
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Save the base64 string to the qr_code field
        validated_data['qr_code'] = qr_base64

        # Create the user instance
        user = User.objects.create(**validated_data)

        return user
