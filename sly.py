import os
import urllib.request
import zipfile
import argparse
import json

failed_downloads = []
tools_without_urls = []
tools = []

def download_and_extract_zip(url, destination):
    try:
        zip_file_name = os.path.basename(url)
        zip_path = os.path.join(destination, zip_file_name)
        extraction_path = os.path.join(destination, os.path.splitext(zip_file_name)[0])

        with urllib.request.urlopen(url) as response:
            with open(zip_path, 'wb') as out_file:
                file_size = int(response.headers['content-length'])
                print(f"Downloading {zip_file_name}")

                downloaded = 0
                chunk_size = 1024
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    out_file.write(chunk)
                    downloaded += len(chunk)
                    percent = downloaded / file_size * 100
                    print(f"Downloaded {percent:.2f}%", end="\r", flush=True)
        print("\n")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            os.makedirs(extraction_path, exist_ok=True)
            zip_ref.extractall(extraction_path)
        os.remove(zip_path)
        return True
    except Exception as e:
        print(f"\nError downloading or extracting {url}: {e}")
        return False

def download_file(url, destination):
    try:
        if url.endswith('.zip'):
            return download_and_extract_zip(url, destination)
        else:
            file_path = os.path.join(destination, os.path.basename(url))
            with urllib.request.urlopen(url) as response:
                with open(file_path, 'wb') as out_file:
                    file_size = int(response.headers['content-length'])
                    print(f"Downloading {os.path.basename(file_path)}")

                    downloaded = 0
                    chunk_size = 1024
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        out_file.write(chunk)
                        downloaded += len(chunk)
                        percent = downloaded / file_size * 100
                        print(f"Downloaded {percent:.2f}%", end="\r", flush=True)
            print("\n")
            return True
    except Exception as e:
        print(f"\nError downloading {url}: {e}")
        return False

def copy_file(source, destination):
    try:
        if os.path.exists(source):
            total_size = os.path.getsize(source)
            copied = 0
            chunk_size = 1024 * 1024  # 1MB chunk size

            with open(source, 'rb') as src_file:
                with open(os.path.join(destination, os.path.basename(source)), 'wb') as dst_file:
                    while True:
                        chunk = src_file.read(chunk_size)
                        if not chunk:
                            break
                        dst_file.write(chunk)
                        copied += len(chunk)
                        percent = (copied / total_size) * 100
                        print(f"Copying {os.path.basename(source)} - {percent:.2f}%", end="\r", flush=True)
            print("\n")
            return True
        else:
            print(f"File not found: {source}")
            return False
    except Exception as e:
        print(f"\nError copying {source}: {e}")
        return False

def main(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for tool in tools:
        if not tool["paths"]:
            tools_without_urls.append(tool["name"])
            continue

        for path in tool["paths"]:
            if path.startswith("http://") or path.startswith("https://"):
                if not download_file(path, destination):
                    failed_downloads.append(path)
            else:
                if not copy_file(path, destination):
                    failed_downloads.append(path)

    if failed_downloads:
        print("\nFailed to download the following tools:")
        for path in failed_downloads:
            print(f"- {path}")

    if tools_without_urls:
        print("\nThe following tools didn't have any URLs defined:")
        for tool in tools_without_urls:
            print(f"- {tool}")

if __name__ == "__main__":
    with open('tools.json', 'r') as file:
        tools = json.load(file)

    parser = argparse.ArgumentParser(description='This script downloads and/or copies a predefined list of tools to a specified directory. It handles both direct file copying and downloading from URLs, including handling zip files.')

    parser.add_argument('-d', '--destination', help='The full path to the destination directory where tools will be downloaded/copied. If not specified, it defaults to a subdirectory in the current working directory.')
    parser.add_argument('-f', '--folder', default="sly", help='Name of the subdirectory in the current working directory to use as the default destination. Defaults to "sly".')

    args = parser.parse_args()
    destination = args.destination if args.destination else os.path.join(os.getcwd(), args.folder)
    main(destination)