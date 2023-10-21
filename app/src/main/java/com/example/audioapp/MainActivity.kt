package com.example.audioapp
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import java.io.BufferedReader
import java.io.InputStreamReader

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val dataTextView = findViewById<TextView>(R.id.dataTextView)

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
        } catch (e: Exception) {
            e.printStackTrace()
            dataTextView.text = "Failed to read data from the file."
        }
    }
}
