package com.example.audioapp
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import java.io.BufferedReader
import java.io.InputStreamReader

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val dataTextView = findViewById<TextView>(R.id.dataTextView)
        val loadButton = findViewById<Button>(R.id.loadButton)
        val stopButton = findViewById<Button>(R.id.stopButton)

        loadButton.setOnClickListener {
            try {
                val fileInputStream = assets.open("output.txt")
                val bufferedReader = BufferedReader(InputStreamReader(fileInputStream))
                val stringBuilder = StringBuilder()
                var line: String?

                while (bufferedReader.readLine().also { line = it } != null) {
                    stringBuilder.append(line).append("\n")
                }

                fileInputStream.close()
                dataTextView.text = stringBuilder.toString()

                // Show the "Stop Display" button and hide the "Load Data" button
                loadButton.visibility = View.GONE
                stopButton.visibility = View.VISIBLE
            } catch (e: Exception) {
                e.printStackTrace()
                dataTextView.text = "Failed to read data from the file."
            }
        }

        stopButton.setOnClickListener {
            // Clear the data and show the "Load Data" button while hiding the "Stop Display" button
            dataTextView.text = "Click the 'Load Data' button to load data."
            loadButton.visibility = View.VISIBLE
            stopButton.visibility = View.GONE
        }
    }
}
