//
//  SearchViewController.swift
//  Hotelzzz
//
//  Created by Steve Johnson on 3/22/17.
//  Copyright © 2017 Hipmunk, Inc. All rights reserved.
//

import Foundation
import WebKit
import UIKit


private let dateFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateFormat = "YYYY-mm-dd"
    return formatter
}()


class SearchViewController: UIViewController {
    lazy var webView: WKWebView = {
        let webView = WKWebView()
        webView.translatesAutoresizingMaskIntoConstraints = false

        self.view.addSubview(webView)
        self.view.addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "H:|[webView]|", options: [], metrics: nil, views: ["webView": webView]))
        self.view.addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "V:|[webView]|", options: [], metrics: nil, views: ["webView": webView]))
        return webView
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    func search(location: String, dateStart: Date, dateEnd: Date) {
        self.webView.load(URLRequest(url: URL(string: "http://localhost:3000")!))

        let paramsJSONData = try! JSONSerialization.data(
            withJSONObject: [
                "location": location,
                "dateStart": dateFormatter.string(from: dateStart),
                "dateEnd": dateFormatter.string(from: dateEnd)
            ],
            options: [])
        let paramsJSON: String = String(data: paramsJSONData, encoding: .utf8)!

        /* At some point, you will need to run this JS: */
        /*
        self.webView.evaluateJavaScript(
            "window.JSAPI.runHotelSearch(\(paramsJSON))",
            completionHandler: nil)
         */
    }
}
