from pypdf import PdfWriter
def merge_pdfs(input_paths: list[str], output_path: str):
    """Merges multiple PDF files into a single PDF.
    """
    merger = PdfWriter()
    for path in input_paths:
        try:
            merger.append(path)
            print(f"Successfully added: {path}")
        except FileNotFoundError:
            print(f"Error: File not found - {path}")
        except Exception as e:
            print(f"Error processing {path}: {e}")

    try:
        merger.write(output_path)
        print(f"Successfully merged PDFs into: {output_path}")
    except Exception as e:
        print(f"Error writing merged PDF: {e}")
    finally:
        merger.close()


pdf_files_to_merge = ["1.pdf", "2.pdf"]  
output_file = "merged_document.pdf"
merge_pdfs(pdf_files_to_merge, output_file)
