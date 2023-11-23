## Getting Started

1. **Set Up Virtual Environment:**

   ```bash
   # Navigate to the project directory

   # Create a virtual environment
   python3 -m venv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure AWS Credentials:**

   - Set the AWS credentials in the `.env` file which will be shared by the author.

     ```plaintext
     AWS_ACCESS_KEY_ID=your_access_key_id
     AWS_SECRET_ACCESS_KEY=your_secret_access_key
     AWS_DEFAULT_REGION=your_aws_region
     S3_BUCKET_NAME=your_bucket_name
     S3_FILE_KEY=your_file_key
     ```

3. **Run the Project:**

   ```bash
   python runner.py
   ```

4. **Notes:**

   - Replace placeholder values in `.env` with the AWS credentials shared by the author.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests.
