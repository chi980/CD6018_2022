var mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(37.5794251, 126.9214472), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
  };

// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);

if (navigator.geolocation) {
  // GeoLocation을 이용해서 접속 위치를 얻어옵니다
  navigator.geolocation.getCurrentPosition(function (pos) {
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

    // map.setCenter(currentPos);
  });
} else {
  // HTML5의 GeoLocation을 사용할 수 없을때

  var currentPos = new kakao.maps.LatLng(37.5794251, 126.9214472);
  alert("현재 위치를 찾을 수 없습니다!");
}

// 나의 위치 마커 이미지의 이미지 주소입니다
var myMarkerImgSrc = "/static/images/my_marker.png";
myImgSize = new kakao.maps.Size(22, 22);
myMarkerImage = new kakao.maps.MarkerImage(myMarkerImgSrc, myImgSize);

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
    location: new kakao.maps.LatLng(37.5794251, 126.9214472),
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

  // 검색결과 목록의 자식 Element를 제거하는 함수입니다
  function removeAllChildNods(el) {
    while (el.hasChildNodes()) {
      el.removeChild(el.lastChild);
    }
  }
}

function displayStepswindow() {
  document.getElementById("steps").style.display = "none";
}

//recommend_form_list = document.getElementsByClassName("favorite_form")
recommended_id_list = document.getElementsByClassName("location_id");
//recommended_id_input_list = document.getElementsByClassName("location_id_input")
recommended_div_list = document.getElementsByClassName("steps__bg");
recommended_name_list = document.getElementsByClassName("location_name");
recommended_address_list = document.getElementsByClassName("location_address");
recommended_lot_address_list = document.getElementsByClassName(
  "location_lot_address"
);
recommended_phone_list = document.getElementsByClassName("location_phone");
recommended_time_list = document.getElementsByClassName("location_time");
recommended_url_list = document.getElementsByClassName("location_url");
recommended_is_animal_in_list = document.getElementsByClassName(
  "location_is_animal_in"
);
recommended_star_list = document.getElementsByClassName("location_star");
location_btn_list = document.getElementsByClassName("favorite_btn");

kakao.maps.event.addListener(map, "idle", function () {
  console.log("idle상태입니다.");
  // 지도 영역정보를 얻어옵니다
  var bounds = map.getBounds();

  // 영역정보의 남서쪽 정보를 얻어옵니다
  var swLatlng = bounds.getSouthWest();

  // 영역정보의 북동쪽 정보를 얻어옵니다
  var neLatlng = bounds.getNorthEast();
  var mapinfo = {
    swLatlng: swLatlng,
    neLatlng: neLatlng,
  };
  var message =
    "<p>영역좌표는 남서쪽 위도, 경도는  " + swLatlng.toString() + "이고 <br>";
  message += "북동쪽 위도, 경도는  " + neLatlng.toString() + "입니다 </p>";
  console.log(message);
  $.ajax({
    url: "/main/recommended/",
    type: "POST",
    headers: {
      "X-CSRFTOKEN": "{{ csrf_token }}",
    },
    data: JSON.stringify(mapinfo),
    success: function (data) {
      // AJAX 통신 성공시 받은 데이터를 console에 print

      console.log("성공~");
      //      console.log(data.locations_cafe);
      //      console.log(data.locations_restau);
      //      console.log(data.locations_pet);
      var location_cafe = JSON.parse(data.locations_cafe) || null;
      var location_food = JSON.parse(data.locations_restau) || null;
      var location_pet = JSON.parse(data.locations_pet) || null;
      // console.log(location_pet[0] + "oo");

      for (var i = 0; i < recommended_div_list.length; i++)
        recommended_div_list[i].style.visibility = "hidden";
      if (data.recommended) {
        var location_favorite = JSON.parse(data.recommended_favorite) || null;
        var recommended = JSON.parse(data.recommended);
        for (var i = 0; i < recommended.length; i++) {
          // div->innertext, p->innerhtml
          recommended_div_list[i].style.visibility = "visible";
          recommended_id_list[i].innerHTML = recommended[i].location_id;
          //            recommended_id_input_list.value = recommended[i].location_id;
          location_btn_list[i].setAttribute(
            "data-value",
            recommended[i].location_id
          );
          recommended_name_list[i].innerHTML = recommended[i].location__name;
          recommended_address_list[i].innerText =
            recommended[i].location__address;
          recommended_phone_list[i].innerText =
            recommended[i].location__lot_address;
          recommended_time_list[i].innerText = recommended[i].location__time;
          recommended_url_list[i].href = recommended[i].location__url;
          recommended_url_list[i].innerHTML = recommended[i].location__url;
          recommended_star_list[i].innerText = recommended[i].star_avg;
          console.log(location_favorite);
          if (location_favorite[i] == true)
            location_btn_list[i].children[0].src =
              "/static/images/like_sel.png";
          else
            location_btn_list[i].children[0].src =
              "/static/images/like_no_sel.png";
        }
      }

      createFoodMarkers(location_food);
      createCafeMarkers(location_cafe);
      createPetMarkers(location_pet);
    },
    error: function (data) {
      // AJAX 통신 실패시 alert창
      //            alert(data.status); // the status code
      console.log(data);
      if (data.responseJSON.error) {
        alert(data.responseJSON.error);
      }
    },
  });
});

var foodMarkers = [],
  cafeMarkers = [],
  petMarkers = [];

changeMarker("cafe");

var foodMarkerImgSrc = "/static/images/food_marker.png",
  cafeMarkerImgSrc = "/static/images/cafe_marker.png",
  petMarkerImgSrc = "/static/images/pet_marker.png";

// 마커이미지의 주소와, 크기, 옵션으로 마커 이미지를 생성하여 리턴하는 함수입니다
function createMarkerImage(src, size) {
  var markerImage = new kakao.maps.MarkerImage(src, size);
  return markerImage; // 마커 위에 커스텀오버레이를 표시합니다
}
// 좌표와 마커이미지를 받아 마커를 생성하여 리턴하는 함수입니다
function createMarker(name, position, image, clickable) {
  var marker = new kakao.maps.Marker({
    title: name,
    position: position,
    image: image,
    clickable: clickable,
  });

  kakao.maps.event.addListener(marker, "click", function () {
    var iwContent = '<div style="padding:5px;">' + marker.getTitle() + "</div>"; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
    var infowindow = new kakao.maps.InfoWindow({
      map: map, // 인포윈도우가 표시될 지도
      position: marker.getPosition(),
      content: iwContent,
      removable: true,
    });
    infowindow.open(map, marker);
  });
  return marker;
}

// 음식점 마커를 생성하고 음식점 마커 배열에 추가하는 함수입니다
function createFoodMarkers(location_food) {
  for (var i = 0; i < location_food.length; i++) {
    var imageSize = new kakao.maps.Size(32, 40);

    // 마커이미지와 마커를 생성합니다
    var markerImage = createMarkerImage(foodMarkerImgSrc, imageSize),
      marker = createMarker(
        location_food[i].name,
        new kakao.maps.LatLng(
          location_food[i].latitude,
          location_food[i].longitude
        ),
        markerImage,
        true
      );
    // 생성된 마커를 음식점 마커 배열에 추가합니다
    foodMarkers.push(marker);
  }
}

// 음식점 마커들의 지도 표시 여부를 설정하는 함수입니다
function setFoodMarkers(map) {
  for (var i = 0; i < foodMarkers.length; i++) {
    foodMarkers[i].setMap(map);
  }
}

// 카페 마커를 생성하고 카페 마커 배열에 추가하는 함수입니다
function createCafeMarkers(location_cafe) {
  for (var i = 0; i < location_cafe.length; i++) {
    var imageSize = new kakao.maps.Size(32, 40);

    // 마커이미지와 마커를 생성합니다
    var markerImage = createMarkerImage(cafeMarkerImgSrc, imageSize),
      marker = createMarker(
        location_cafe[i].name,
        new kakao.maps.LatLng(
          location_cafe[i].latitude,
          location_cafe[i].longitude
        ),
        markerImage,
        true
      );
    // 생성된 마커를 카페 마커 배열에 추가합니다
    cafeMarkers.push(marker);
  }
}

// 카페 마커들의 지도 표시 여부를 설정하는 함수입니다
function setCafeMarkers(map) {
  for (var i = 0; i < cafeMarkers.length; i++) {
    cafeMarkers[i].setMap(map);
  }
}
// 애견관련 마커를 생성하고 애견 마커 배열에 추가하는 함수입니다
function createPetMarkers(location_pet) {
  for (var i = 0; i < location_pet.length; i++) {
    var imageSize = new kakao.maps.Size(32, 40);

    // 마커이미지와 마커를 생성합니다
    var markerImage = createMarkerImage(petMarkerImgSrc, imageSize),
      marker = createMarker(
        location_pet[i].name,
        new kakao.maps.LatLng(
          location_pet[i].latitude,
          location_pet[i].longitude
        ),
        markerImage,
        true
      );
    // 생성된 마커를 애견 마커 배열에 추가합니다
    petMarkers.push(marker);
  }
}
// 애견 마커들의 지도 표시 여부를 설정하는 함수입니다
function setPetMarkers(map) {
  for (var i = 0; i < petMarkers.length; i++) {
    petMarkers[i].setMap(map);
  }
}

// 카테고리를 클릭했을 때 type에 따라 카테고리의 스타일과 지도에 표시되는 마커를 변경합니다
function changeMarker(type) {
  var foodMenu = document.getElementById("foodMenu");
  var cafeMenu = document.getElementById("cafeMenu");
  var petMenu = document.getElementById("petMenu");

  // 음식점 카테고리가 클릭됐을 때
  if (type === "food") {
    // 커피숍 카테고리를 선택된 스타일로 변경하고
    foodMenu.className = "menu_selected";

    // 카페와 펫 카테고리는 선택되지 않은 스타일로 바꿉니다
    cafeMenu.className = "";
    petMenu.className = "";

    // 음식점 마커들만 지도에 표시하도록 설정합니다
    setFoodMarkers(map);
    setCafeMarkers(null);
    setPetMarkers(null);
  } else if (type === "cafe") {
    // 카페 카테고리가 클릭됐을 때

    // 카페 카테고리를 선택된 스타일로 변경하고
    foodMenu.className = "";
    cafeMenu.className = "menu_selected";
    petMenu.className = "";

    // 카페 마커들만 지도에 표시하도록 설정합니다
    setFoodMarkers(null);
    setCafeMarkers(map);
    setPetMarkers(null);
  } else if (type === "pet") {
    // 펫 카테고리가 클릭됐을 때

    // 펫 카테고리를 선택된 스타일로 변경하고
    foodMenu.className = "";
    cafeMenu.className = "";
    petMenu.className = "menu_selected";

    // 펫 마커들만 지도에 표시하도록 설정합니다
    setFoodMarkers(null);
    setCafeMarkers(null);
    setPetMarkers(map);
  }
}
//console.log(recommended_favorite_list)
//for(var i=0;i<recommend_form_list.length;i++)
//{
//    recommend_form_list[i].addEventListener("submit",function(event){
//
//        event.preventDefault();
//    })
//}

for (var i = 0; i < location_btn_list.length; i++) {
  location_btn_list[i].addEventListener("click", (event) => {
    console.log(event.currentTarget.getAttribute("data-value"));
    img = event.currentTarget.children[0];
    console.log(img);
    var location_info = {
      location_id: event.currentTarget.getAttribute("data-value"),
    };
    $.ajax({
      url: "/main/favorites/",
      type: "POST",
      headers: {
        "X-CSRFTOKEN": "{{ csrf_token }}",
      },
      data: JSON.stringify(location_info),
      success: function (data) {
        console.log(data);
        if (data == "True") {
          //등록
          img.src = "/static/images/like_sel.png";
        } else {
          //삭제
          img.src = "/static/images/like_no_sel.png";
        }
      },
      error: function (data) {
        console.log(data);
      },
    });
  });
}

// 인포윈도우를 표시하는 클로저를 만드는 함수입니다
function makeClickListener(map, marker, infowindow) {
  return function () {
    infowindow.open(map, marker);
  };
}
