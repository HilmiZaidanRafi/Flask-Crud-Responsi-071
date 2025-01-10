// Modal functions
function showAddModal() {
    document.getElementById('addModal').style.display = 'block';
}

function hideAddModal() {
    document.getElementById('addModal').style.display = 'none';
    document.getElementById('addModal').querySelector('form').reset();
}

function showEditModal(nim, nama, asal) {
    document.getElementById('edit_nim').value = nim;
    document.getElementById('edit_nama').value = nama;
    document.getElementById('edit_asal').value = asal;
    document.getElementById('editModal').style.display = 'block';
}

function hideEditModal() {
    document.getElementById('editModal').style.display = 'none';
    document.getElementById('editModal').querySelector('form').reset();
}

// Delete confirmation
function confirmDelete(nim) {
    if (confirm('Apakah Anda yakin ingin menghapus data ini?')) {
        window.location.href = `/delete/${nim}`;
    }
}

// Close modals when clicking outside
window.onclick = function(event) {
    if (event.target.className === 'modal') {
        event.target.style.display = 'none';
    }
}

// Flash messages
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 3000);
    });
});
