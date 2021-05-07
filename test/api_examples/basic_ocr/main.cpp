#include <iostream>
#include <fstream>

#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

// argc[1] -> language
// argc[2] -> path to the image
// argc[3] -> output file

int main(int argv, char** argc) {
    char * out_text;

    tesseract::TessBaseAPI* api = new tesseract::TessBaseAPI();

    std::cout<<"[info]: argc[1]: "<<argc[1]<<std::endl;
    std::cout<<"[info]: argc[2]: "<<argc[2]<<std::endl;
    std::cout<<"[info]: argc[3]: "<<argc[3]<<std::endl;

    // Initialize tesseract-ocr with English, without specifying tessdata path
    if(api->Init(nullptr, argc[1])) {
        std::cerr<<"Could not initialize tesseract.\n";
        exit(1);
    }

    // Open input image with leptonica library
    Pix* image = pixRead(argc[2]);
    api->SetImage(image);

    // Get OCR result
    out_text = api->GetUTF8Text();

    std::ofstream file;
    file.open(argc[3]);
    if(file.is_open()) {
        file << out_text << std::endl;
    }
    file.close();

    // Destroy used object and release memory
    api->End();
    delete api;
    delete [] out_text;
    pixDestroy(&image);

    return 0;
}
