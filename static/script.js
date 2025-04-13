function loadMemos() {
    $.get('/memos', function(data) {
        $('#memoList').empty();
        data.forEach((memo, idx) => {
            $('#memoList').append(`
                <li>
                    <strong>${memo.title}</strong>: ${memo.content}
                    <button onclick="editMemo(${memo.id})">수정</button>
                    <button onclick="deleteMemo(${memo.id})">삭제</button>
                </li>
            `);
        });
    });
}

function addMemo() {
    const title = $('#title').val();
    const content = $('#content').val();
    $.ajax({
        type: 'POST',
        url: '/memos',
        contentType: 'application/json',
        data: JSON.stringify({ title, content }),
        success: loadMemos
    });
}

function editMemo(id) {
    const title = prompt('새 제목:');
    const content = prompt('새 내용:');
    $.ajax({
        type: 'PUT',
        url: `/memos/${id}`,
        contentType: 'application/json',
        data: JSON.stringify({ title, content }),
        success: loadMemos
    });
}

function deleteMemo(id) {
    $.ajax({
        type: 'DELETE',
        url: `/memos/${id}`,
        success: loadMemos
    });
}

$('#addBtn').click(addMemo);
$(document).ready(loadMemos);
