import requests
import time
import hashlib

URL_OF_THESERVER = "http://server:8080/"
PATH_OF_FILE = '/clientdata/FileReceived.txt'

def fetchFile_from_Server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(PATH_OF_FILE, 'wb') as f:
                f.write(response.content)
            return PATH_OF_FILE, response.headers.get('Checksum')
        else:
            response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to download the file: {e}")
        return None, None

def computeSHA256_Checksum(Filepath):
    #Computes the SHA-256 checksum of a file.
    hasher256 = hashlib.sha256()
    with open(Filepath, 'rb') as file:
        while chunk := file.read(8192):
            hasher256.update(chunk)
    return hasher256.hexdigest()

def verifyChecksum(pathOfFile, ChecksumReceived):
    #Verifies that a given file's checksum matches the expected_checksum.
    calculatedChecksum = computeSHA256_Checksum(pathOfFile)
    return calculatedChecksum == ChecksumReceived

def main():
    print("Starting file download")
    fileDownloaded, ChecksumReceived = fetchFile_from_Server(URL_OF_THESERVER)
    
    if fileDownloaded is None or ChecksumReceived is None:
        print("Failed to download file or checksum is missing.")
        return  # Exit if failed to download

    print(f"File downloaded: {fileDownloaded}")
    print(f"Received Checksum: {ChecksumReceived}")
    
    is_checksum_valid = verifyChecksum(fileDownloaded, ChecksumReceived)
    if is_checksum_valid:
        print("Success: File received and verified successfully!")
    else:
        print("Error: Checksum does not match.")
        
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Program terminated.")
    

if __name__ == '__main__':
    main()
