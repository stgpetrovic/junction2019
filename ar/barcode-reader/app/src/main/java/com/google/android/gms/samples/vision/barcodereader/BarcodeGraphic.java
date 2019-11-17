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

import android.app.AlertDialog;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Picture;
import android.graphics.PorterDuff;
import android.graphics.RectF;
import android.os.AsyncTask;
import android.util.Log;
import android.view.ViewGroup;
import android.view.ViewGroup.MarginLayoutParams;
import android.widget.ImageView;
import android.widget.LinearLayout;

import com.caverock.androidsvg.SVG;
import com.caverock.androidsvg.SVGParseException;
import com.google.android.gms.samples.vision.barcodereader.ui.camera.GraphicOverlay;
import com.google.android.gms.vision.barcode.Barcode;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URI;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

/**
 * Graphic instance for rendering barcode position, size, and ID within an associated graphic
 * overlay view.
 */
public class BarcodeGraphic extends GraphicOverlay.Graphic {

    private long lastEvent;

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
    public Paint mProductPaint;
    private volatile Barcode mBarcode;

    BarcodeGraphic(GraphicOverlay overlay) {
        super(overlay);
        init();

        mRectPaint = new Paint();
        mRectPaint.setColor(Color.YELLOW);
        mRectPaint.setStyle(Paint.Style.STROKE);
        mRectPaint.setStrokeWidth(4.0f);

        mProductPaint = new Paint();
        mProductPaint.setColor(Color.GREEN);
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
            mOverlay.getIv().setImageDrawable(null);
            return;
        }

        // Draws the bounding box around the barcode.
        RectF rect = new RectF(barcode.getBoundingBox());
        rect.left = translateX(rect.left);
        rect.top = translateY(rect.top);
        rect.right = translateX(rect.right);
        rect.bottom = translateY(rect.bottom);
        canvas.drawRect(rect, mRectPaint);

        if (java.lang.System.currentTimeMillis() - lastEvent > 200) {
            lastEvent = java.lang.System.currentTimeMillis();
            if (!nameC.containsKey(barcode.rawValue)) {
                new CallAPI(canvas, barcode.rawValue, rect.left - 50, rect.top - 50).execute("http://brahle.com:5000/ean/" + barcode.rawValue);
            }
        }

        if (nameC.containsKey(barcode.rawValue)) {
            mOverlay.getIv().setImageResource(drawC.get(barcode.rawValue));

            mOverlay.getIv().layout((int)rect.left-450, (int)rect.top-450, (int)rect.top, (int) rect.bottom);

            canvas.drawText(nameC.get(barcode.rawValue), rect.left-50, rect.top-50, mProductPaint);
        }
    }

    @Override
    public void hide() {
        mOverlay.getIv().setImageDrawable(null);
    }

    HashMap<String, String> nameC = new HashMap<>();
    HashMap<String, Integer> drawC= new HashMap<>();

    public class CallAPI extends AsyncTask<String, String, String> {

        private final Canvas canvas;
        private final float top;
        private final float left;
        private final String barcode;

        public CallAPI(Canvas canvas, String barcode, float left, float top){
            //set context variables if required
        this.canvas = canvas;
        this.barcode=barcode;
        this.left=left;
        this.top=top;
        }

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }

        @Override
        protected String doInBackground(String... params) {
            String urlString = params[0]; // URL to call
            OutputStream out = null;

            try {
                //Create a URL object holding our url
                URL myUrl = new URL(urlString);
                //Create a connection
                HttpURLConnection connection =(HttpURLConnection)
                        myUrl.openConnection();
                //Set methods and timeouts
                connection.setRequestMethod("GET");
                connection.setReadTimeout(15000);
                connection.setConnectTimeout(15000);

                //Connect to our url
                connection.connect();
                //Create a new InputStreamReader
                InputStreamReader streamReader = new
                        InputStreamReader(connection.getInputStream());
                //Create a new buffered reader and String Builder
                BufferedReader reader = new BufferedReader(streamReader);
                StringBuilder stringBuilder = new StringBuilder();
                //Check if the line we are reading is not null
                String inputLine;
                while((inputLine = reader.readLine()) != null){
                    stringBuilder.append(inputLine);
                }
                //Close our InputStream and Buffered reader
                reader.close();
                streamReader.close();
                //Set our result equal to our stringBuilder
                Log.d("Aaaa", stringBuilder.toString());
                return stringBuilder.toString();
            }
            catch(IOException e){
                e.printStackTrace();
            }
            return "";
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            String[] parts = s.toString().split("\\|");
                    if (parts.length != 4) {
                        return;
                    }
            int drawing = kosara(parts[2]);
            String name = parts[3];
            nameC.put(barcode, name);
            drawC.put(barcode, drawing);
        }

        int kosara(String kosara) {
            if (kosara.equals("0_0.png")) {
                mProductPaint.setColor(Color.RED);
                return R.drawable.kosara0_0;
            }
            if (kosara.equals("0_1.png")) {
                mProductPaint.setColor(Color.RED);
                return R.drawable.kosara0_1;
            }
            if (kosara.equals("0_2.png")) {
                mProductPaint.setColor(Color.YELLOW);
                return R.drawable.kosara0_2;
            }
            if (kosara.equals("1_0.png")) {
                mProductPaint.setColor(Color.RED);
                return R.drawable.kosara1_0;
            }
            if (kosara.equals("1_1.png")) {
                mProductPaint.setColor(Color.YELLOW);
                return R.drawable.kosara1_1;
            }
            if (kosara.equals("1_2.png")) {
                mProductPaint.setColor(Color.GREEN);
                return R.drawable.kosara1_2;
            }
            if (kosara.equals("2_0.png")) {
                mProductPaint.setColor(Color.YELLOW);
                return R.drawable.kosara2_0;
            }
            if (kosara.equals("2_1.png")) {
                mProductPaint.setColor(Color.GREEN);
                return R.drawable.kosara2_1;
            }
            if (kosara.equals("2_2.png")) {
                mProductPaint.setColor(Color.GREEN);
                return R.drawable.kosara2_2;
            }
            return R.drawable.kosara0_0;
        }
    }

}
