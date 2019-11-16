/*
 * Copyright (C) The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.google.android.gms.samples.vision.barcodereader;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.RectF;

import com.google.android.gms.samples.vision.barcodereader.ui.camera.GraphicOverlay;
import com.google.android.gms.vision.barcode.Barcode;

import java.util.HashMap;
import java.util.Map;

/**
 * Graphic instance for rendering barcode position, size, and ID within an associated graphic
 * overlay view.
 */
public class BarcodeGraphic extends GraphicOverlay.Graphic {

    class Product {
        public String ean;
        public String name;
        public int goodness;
        public int sustainability;
        public double price;

        public Product(String ean,String name, int goodness, int sustainability, double price) {
            this.ean=ean;
            this.name = name;
            this.goodness=goodness;
            this.sustainability=sustainability;
            this.price=price;
        }

        @Override
        public String toString() {
            return this.name + " (" + price + "€)";
        }
    }

    private static final Map<String, Product> PRODUCTS = new HashMap<String, Product>();

    private void init() {
        PRODUCTS.put("6415600548588", new Product("6415600548588","Battery No Calories Peach-Raspberry", 25,80,4.5));
        PRODUCTS.put("7050370109103", new Product("7050370109103","Pähkinä-hedelmäsekoitus", 85,70,6.29));
        PRODUCTS.put("7394376616747", new Product("7394376616747","Oatly cold brew latte", 78,77,2.59));
        PRODUCTS.put("7310100574718", new Product("7310100574718","Good'N'Go oatmeal", 93,96,0.99));
        PRODUCTS.put("5706779062243", new Product("5706779062243","Earth Control", 77,67,5.00));
    }

    private int mId;

    private static int mCurrentColorIndex = 0;

    private Paint mRectPaint;
    private Paint mTextPaint;
    private Paint mProductPaint;
    private volatile Barcode mBarcode;

    BarcodeGraphic(GraphicOverlay overlay) {
        super(overlay);
        init();

        mRectPaint = new Paint();
        mRectPaint.setColor(Color.CYAN);
        mRectPaint.setStyle(Paint.Style.STROKE);
        mRectPaint.setStrokeWidth(4.0f);

        mTextPaint = new Paint();
        mTextPaint.setColor(Color.CYAN);
        mTextPaint.setTextSize(36.0f);

        mProductPaint = new Paint();
        mProductPaint.setColor(Color.YELLOW);
        mProductPaint.setTextSize(50.0f);
    }

    public int getId() {
        return mId;
    }

    public void setId(int id) {
        this.mId = id;
    }

    public Barcode getBarcode() {
        return mBarcode;
    }

    /**
     * Updates the barcode instance from the detection of the most recent frame.  Invalidates the
     * relevant portions of the overlay to trigger a redraw.
     */
    void updateItem(Barcode barcode) {
        mBarcode = barcode;
        postInvalidate();
    }

    /**
     * Draws the barcode annotations for position, size, and raw value on the supplied canvas.
     */
    @Override
    public void draw(Canvas canvas) {
        Barcode barcode = mBarcode;
        if (barcode == null) {
            return;
        }

        // Draws the bounding box around the barcode.
        RectF rect = new RectF(barcode.getBoundingBox());
        rect.left = translateX(rect.left);
        rect.top = translateY(rect.top);
        rect.right = translateX(rect.right);
        rect.bottom = translateY(rect.bottom);
        canvas.drawRect(rect, mRectPaint);

        // Draws a label at the bottom of the barcode indicate the barcode value that was detected.
        canvas.drawText(barcode.rawValue, rect.left, rect.bottom, mTextPaint);
        String url = "https://public.keskofiles.com/f/k-ruoka/product/5706779062243?w=400&h=250&auto=format&fm=jpg&fit=fillmax&fill=solid&fill-color=ffffff&cs=srgb";


        if (PRODUCTS.containsKey(barcode.rawValue)) {
            canvas.drawText(PRODUCTS.get(barcode.rawValue).toString(), rect.left-20, rect.top-50, mProductPaint);
        }
    }
}
