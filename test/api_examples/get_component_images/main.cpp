#include <iostream>
#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

int main(int argv, char** argc)
{
    std::cout<<"[info]: argc[1]: "<<argc[1]<<std::endl;
    std::cout<<"[info]: argc[2]: "<<argc[2]<<std::endl;

    Pix* image = pixRead(argc[2]);
    tesseract::TessBaseAPI* api = new tesseract::TessBaseAPI();
    api->Init(nullptr, argc[1]);
    api->SetImage(image);
    Boxa* boxes = api->GetComponentImages(tesseract::RIL_TEXTLINE, true, nullptr, nullptr);
    std::cout<<"Found textline image components: "<<boxes->n<<std::endl;
    for(int i = 0; i <boxes->n; ++i) {
        Box* box = boxaGetBox(boxes, i, L_CLONE);
        api->SetRectangle(box->x, box->y, box->w, box->h);
        char* ocr_result = api->GetUTF8Text();
        int conf = api->MeanTextConf();
        fprintf(stdout, "Box[%d]: x=%d, y=%d, w=%d, h=%d, confidence: %d, text: %s",
                i, box->x, box->y, box->w, box->h, conf, ocr_result);
        boxDestroy(&box);
    }

    return 0;
}