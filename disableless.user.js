// ==UserScript==
// @name         北京八中云课堂提前进教室
// @namespace    http://tampermonkey.net/
// @version      0.1.0
// @description  使北京八中的同学能够提前进入教室
// @author       zyc2024
// @match        https://zhibostu.changyan.com/courseStudentWeb/*
// @grant        none
// ==/UserScript==

(function () {
	"use strict";
	var _i = document.getElementsByClassName("tabs-nav-list");
	setTimeout(function () {
		var btn = document.createElement("button");
		btn.id = "unlockButton";
		btn.textContent = "一键解除锁定";
		btn.style.background = "#4f8cff";
		btn.style.color = "#fff";
		btn.style.border = "none";
		btn.style.borderRadius = "6px";
		btn.style.padding = "5px 14px";
		btn.style.fontSize = "23px";
		btn.style.fontWeight = "bold";
		btn.style.boxShadow = "0 2px 8px rgba(79, 140, 255, 0.15)";
		btn.style.cursor = "pointer";
		btn.style.transition = "background 0.3s, transform 0.2s";
		btn.style.transform = "scale(0.7)";
		btn.onmouseover = function () {
			this.style.transform = "scale(0.75)";
		};
		btn.onmouseout = function () {
			this.style.transform = "scale(0.7)";
		};
		btn.addEventListener("click", function () {
			Array.from(
				document.getElementsByClassName("ant-btn ant-btn-primary")
			).forEach(function (_o) {
				_o.disabled = false;
			});
			btn.innerText = "已解除锁定";
			btn.style.background = "#28a745";
			btn.disabled = true;
			btn.style.cursor = "not-allowed";
		});
		_i[0].appendChild(btn);
	}, 1000);
})();
