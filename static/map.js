var mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(37.4825508, 126.9732587), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
    mapTypeId: kakao.maps.MapTypeId.ROADMAP, // 지도종류
  };

var positions = [
    {
      title: "디폴트",
      latlng: new kakao.maps.LatLng(37.4825508, 126.9732587),
    },
    {
      title: "동작구1",
      latlng: new kakao.maps.LatLng(37.4881887, 126.9101357),
    },
    {
      title: "동작구2",
      latlng: new kakao.maps.LatLng(37.4872202, 126.909414),
    },
    {
      title: "동작구3",
      latlng: new kakao.maps.LatLng(37.4857688, 126.9779247),
    },
  ],
  selectedMarker = null;

var mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(37.4825508, 126.9732587), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
    mapTypeId: kakao.maps.MapTypeId.ROADMAP, // 지도종류
  };

// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);
// 마커를 표시할 위치와 title 객체 배열입니다

// 나의 위치 마커 이미지의 이미지 주소입니다
var myMarkerImgSrc = "/static/images/my_marker.png";
myImgSize = new kakao.maps.Size(22, 22);
myMarkerImage = new kakao.maps.MarkerImage(myMarkerImgSrc, myImgSize);

// 음식 마커 이미지의 이미지 주소입니다
var foodMarkerImgSrc = "/static/images/food_marker.png";
foodImgSize = new kakao.maps.Size(32, 40);
OverFoodImgSize = new kakao.maps.Size(36, 45);
foodMarkerImage = new kakao.maps.MarkerImage(foodMarkerImgSrc, foodImgSize);
OverFoodMarkerImage = new kakao.maps.MarkerImage(
  foodMarkerImgSrc,
  OverFoodImgSize
);

// 카페 마커 이미지의 이미지 주소입니다
var cafeMarkerImgSrc = "/static/images/cafe_marker.png";
cafeImgSize = new kakao.maps.Size(32, 40);
OverCafeImgSize = new kakao.maps.Size(36, 45);
cafeMarkerImage = new kakao.maps.MarkerImage(cafeMarkerImgSrc, foodImgSize);
OverCafeMarkerImage = new kakao.maps.MarkerImage(
  foodMarkerImgSrc,
  OverCafeImgSize
);
// var count = 0;
// makeMarkers.forEach(function (element) {});
var coContent =
  '<div class="wrap">' +
  '    <div class="info">' +
  '        <div class="title">' +
  "           " +
  //   positions[i].title +
  '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
  "        </div>" +
  '        <div class="body">' +
  // '            <div class="img">' +
  // // '                <img src="https://place.map.kakao.com/820074096" width="73" height="70">' +
  // '           </div>' +
  '	            <div class="desc">' +
  '                	<div class="ellipsis"></div>' +
  '                	<div class="jibun ellipsis">(우) 00000 (지번) 000동 0000 </div>' +
  '               	 <div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div>' +
  "           	 </div>" +
  "       	 </div>" +
  "   	 </div>" +
  "	</div>"; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

for (var i = 0; i < positions.length; i++) {
  // 마커를 생성합니다
  if (positions[i].title == "디폴트")
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      position: positions[i].latlng, // 마커를 표시할 위치
      title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
      image: myMarkerImage, // 마커 이미지
      clickable: false,
    });
  else if (positions[i].title == "동작구1")
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      position: positions[i].latlng, // 마커를 표시할 위치
      title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
      image: foodMarkerImage, // 마커 이미지
      clickable: true,
    });
  else
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      position: positions[i].latlng, // 마커를 표시할 위치
      title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
      image: cafeMarkerImage, // 마커 이미지
      clickable: true,
    });
  var customOverlay = new daum.maps.CustomOverlay({
    position: positions[i].latlng,
    content: coContent,
    xAnchor: 0.33,
    yAnchor: 1.05,
  });
  // kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, customOverlay));
  // kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(customOverlay));
}
marker.setMap(map);
customOverlay.setMap(map);

//커스텀 오버레이 표시
function makeCustomOverlay(map, marker, customOverlay) {
  return function () {
    customOverlay.open(map, marker);
  };
}
function makeOutListener(customOverlay) {
  return function () {
    customOverlay.close();
  };
}

function locationLoadSuccess(pos) {
  // 나의 위치 마커 이미지의 이미지 주소입니다
  var myMarkerImgSrc = "/static/images/my_marker.png";

  // 내 위치 마커 이미지의 이미지 크기 입니다
  var myimageSize = new kakao.maps.Size(22, 22);

  // 나의 마커 이미지를 생성합니다
  var myMarkerImage = new kakao.maps.MarkerImage(myMarkerImgSrc, myimageSize);

  // 현재 위치 받아오기
  var currentPos = new kakao.maps.LatLng(
    pos.coords.latitude,
    pos.coords.longitude
  );

  // 지도 이동(기존 위치와 가깝다면 부드럽게 이동)
  map.panTo(currentPos);

  // 마커 생성
  var marker = new kakao.maps.Marker({
    position: currentPos,
    image: myMarkerImage, // 마커 이미지
    clickable: false,
  });

  // 기존에 마커가 있다면 제거
  marker.setMap(null);
  marker.setMap(map);
}

function locationLoadError(pos) {
  alert("위치 정보를 가져오는데 실패했습니다.");
}

// 1. 내 위치 가져오기 버튼 클릭시
function getCurrentPosBtn() {
  console.log("위치 가져오기 버튼 클릭")
  navigator.geolocation.getCurrentPosition(
    locationLoadSuccess,
    locationLoadError
  );

}

// 2. 중심좌표 변경 이벤트
//https://apis.map.kakao.com/web/sample/addMapCenterChangedEvent/
//kakao.maps.event.addListener(map, 'center_changed', function() {
//    console.log('중심좌표가 변경됩니다.');
//    myMapInfo();
//
//});

// 3. 영역 변경 이벤트
// 지도가 이동, 확대, 축소로 인해 지도영역이 변경되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
//kakao.maps.event.addListener(map, 'bounds_changed', function() {
//    console.log('영역이 변경됩니다.');
//    myMapInfo();
//});
kakao.maps.event.addListener(map, 'idle', function() {
    console.log("idle상태입니다.");
    // 지도 영역정보를 얻어옵니다
    var bounds = map.getBounds();

    // 영역정보의 남서쪽 정보를 얻어옵니다
    var swLatlng = bounds.getSouthWest();

    // 영역정보의 북동쪽 정보를 얻어옵니다
    var neLatlng = bounds.getNorthEast();
    var mapinfo = {
        'swLatlng':swLatlng,
        'neLatlng':neLatlng
    }
    var message = '<p>영역좌표는 남서쪽 위도, 경도는  ' + swLatlng.toString() + '이고 <br>';
    message += '북동쪽 위도, 경도는  ' + neLatlng.toString() + '입니다 </p>';
    console.log(message);
    $.ajax({
        url: 'main/recommended/',
        type: 'POST',
        headers: {
            'X-CSRFTOKEN' : '{{ csrf_token }}'
        },
        data: JSON.stringify(mapinfo),
        success:function(data){
            console.log(data);
        },
        error:function(){
            alert("AJAX 실패~~~~~~~~~");
        }
    });
});
//function myMapInfo(){
//    // 지도 영역정보를 얻어옵니다
//    var bounds = map.getBounds();
//
//    // 영역정보의 남서쪽 정보를 얻어옵니다
//    var swLatlng = bounds.getSouthWest();
//
//    // 영역정보의 북동쪽 정보를 얻어옵니다
//    var neLatlng = bounds.getNorthEast();
//
//    var message = '<p>영역좌표는 남서쪽 위도, 경도는  ' + swLatlng.toString() + '이고 <br>';
//    message += '북동쪽 위도, 경도는  ' + neLatlng.toString() + '입니다 </p>';
//    console.log(message);
//}


// 검색 버튼 클릭시
function keywordSearch() {
  var keyword = $("#keyword").val();
  var markers = [];

  // 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우를 생성합니다
  var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

  // 장소 검색 객체를 생성합니다
  var ps = new kakao.maps.services.Places(map);

  // 검색 옵션 객체
  var searchOption = {
    location: new kakao.maps.LatLng(37.4825508, 126.9732587),
    radius: 1000,
    size: 5,
  };

  // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
  ps.keywordSearch(keyword, placesSearchCB, searchOption);

  // 장소검색이 완료됐을 때 호출되는 콜백함수 입니다
  function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
      // 정상적으로 검색이 완료됐으면
      // 검색 목록과 마커를 표출합니다
      displayPlacesOnSidebar(data);

      // 페이지 번호를 표출합니다
      displayPagination(pagination);
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
      alert("검색 결과가 존재하지 않습니다.");
      return;
    } else if (status === kakao.maps.services.Status.ERROR) {
      alert("검색 결과 중 오류가 발생했습니다.");
      return;
    }
  }

  // 사이드바에 결과 출력 + 마커 생성
  function displayPlacesOnSidebar(places) {
    var listEl = document.getElementById("placesList"),
      menuEl = document.getElementsByClassName("result-list"),
      fragment = document.createDocumentFragment(),
      bounds = new kakao.maps.LatLngBounds(),
      listStr = "";

    // 검색 결과 목록에 추가된 항목들을 제거합니다
    removeAllChildNods(listEl);

    // 지도에 표시되고 있는 마커를 제거합니다
    removeMarker();

    for (var i = 0; i < places.length; i++) {
      // 마커를 생성하고 지도에 표시합니다
      var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
        marker = addMarker(placePosition, i),
        itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

      // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
      // LatLngBounds 객체에 좌표를 추가합니다
      bounds.extend(placePosition);

      // 마커와 검색결과 항목에 mouseover 했을때
      // 해당 장소에 인포윈도우에 장소명을 표시합니다
      // mouseout 했을 때는 인포윈도우를 닫습니다
      (function (marker, title) {
        kakao.maps.event.addListener(marker, "mouseover", function () {
          displayInfowindow(marker, title);
        });

        kakao.maps.event.addListener(marker, "mouseout", function () {
          infowindow.close();
        });

        itemEl.onmouseover = function () {
          displayInfowindow(marker, title);
        };

        itemEl.onmouseout = function () {
          infowindow.close();
        };
      })(marker, places[i].place_name);

      fragment.appendChild(itemEl);
    }

    // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
    listEl.appendChild(fragment);
    menuEl.scrollTop = 0;

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.setBounds(bounds);
  }

  // 검색결과 항목을 Element로 반환하는 함수입니다
  function getListItem(index, places) {
    var el = document.createElement("li"),
      itemStr =
        '<span class="markerbg marker_' +
        (index + 1) +
        '"></span>' +
        '<div class="info">' +
        "   <h5>" +
        places.place_name +
        "</h5>";

    itemStr += '  <span class="tel">' + places.phone + "</span>" + "</div>";

    el.innerHTML = itemStr;
    el.className = "item";

    return el;
  }

  // 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
  function addMarker(position, idx, title) {
    var imageSrc =
        "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png", // 마커 이미지 url, 스프라이트 이미지를 씁니다
      imageSize = new kakao.maps.Size(36, 37), // 마커 이미지의 크기
      imgOptions = {
        spriteSize: new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
        spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
        offset: new kakao.maps.Point(13, 37), // 마커 좌표에 일치시킬 이미지 내에서의 좌표
      },
      markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
      marker = new kakao.maps.Marker({
        position: position, // 마커의 위치
        image: markerImage,
      });

    marker.setMap(map); // 지도 위에 마커를 표출합니다
    markers.push(marker); // 배열에 생성된 마커를 추가합니다

    return marker;
  }

  // 지도 위에 표시되고 있는 마커를 모두 제거합니다
  function removeMarker() {
    for (var i = 0; i < markers.length; i++) {
      markers[i].setMap(null);
    }
    markers = [];
  }

  // 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
  function displayPagination(pagination) {
    var paginationEl = document.getElementById("pagination"),
      fragment = document.createDocumentFragment(),
      i;

    // 기존에 추가된 페이지번호를 삭제합니다
    while (paginationEl.hasChildNodes()) {
      paginationEl.removeChild(paginationEl.lastChild);
    }

    for (i = 1; i <= pagination.last; i++) {
      var el = document.createElement("a");
      el.href = "#";
      el.innerHTML = i;

      if (i === pagination.current) {
        el.className = "on";
      } else {
        el.onclick = (function (i) {
          return function () {
            pagination.gotoPage(i);
          };
        })(i);
      }

      fragment.appendChild(el);
    }
    paginationEl.appendChild(fragment);
  }

  // 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
  // 인포윈도우에 장소명을 표시합니다
  function displayInfowindow(marker, title) {
    var content = '<div style="padding:5px;z-index:1;">' + title + "</div>";

    infowindow.setContent(content);
    infowindow.open(map, marker);
  }

  // 검색결과 목록의 자식 Element를 제거하는 함수입니다
  function removeAllChildNods(el) {
    while (el.hasChildNodes()) {
      el.removeChild(el.lastChild);
    }
  }
}
