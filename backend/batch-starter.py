import os
import glob
# Import the parser function from OCR parser inside app folder
from app.OCRparser import parse_utility_bill 

def run_batch_test(bills_folder="uploads/test_bills"):
    """
    Loops through all PDF bills in the specified folder, 
    runs the parser on each, and prints a summary report.
    """
    pdf_pattern = os.path.join(bills_folder, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        print(f"[-] No PDF files found in '{bills_folder}/'. Please add sample bills first.")
        return

    print(f"[+] Found {len(pdf_files)} PDF bills to test. Starting batch run...\n")
    
    success_count = 0
    fail_count = 0

    for file_path in pdf_files:
        file_name = os.path.basename(file_path)
        print(f"[*] Processing: {file_name}...")
        
        try:
            # Call parser function
            extracted_data = parse_utility_bill(file_path)

            # Below you will need to add the right entries that I will be extracting from the PDF. For now 
            # it should be what we are storing into the database.
            print(f"    SUCCESS -> kwh: {extracted_data.get('kwh')}, Amount: ${extracted_data.get('total_due')}")
            success_count += 1
        # If any errors occure they will be caught here. 
        except Exception as e:
            print(f"    FAILED  -> Error: {str(e)}")
            fail_count += 1
            
        print("-" * 40)

    print(f"\n[=== BATCH TEST COMPLETE ===]")
    print(f"Total Tested: {success_count + fail_count}")
    print(f"Passed:       {success_count}")
    print(f"Failed:       {fail_count}")

if __name__ == "__main__":
    run_batch_test()