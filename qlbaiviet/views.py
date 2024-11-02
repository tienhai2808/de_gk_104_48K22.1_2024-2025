from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import BaiVietForm
from django.contrib import messages

# Create your views here.
# def base(request):
#   return render(request, 'base.html')

def dsbaiviet(request):
  title = 'DANH SÁCH BÀI VIẾT'
  baiviets = BaiViet.objects.all()
  return render(request, 'dsbaiviet.html', {'title': title, 'baiviets': baiviets})

def baiviet(request, idbaiviet=None):
  if idbaiviet:
    title = 'SỬA THÔNG TIN BÀI VIẾT'
    bai_viet = get_object_or_404(BaiViet, id=idbaiviet)
    button = 'Lưu'
  else:
    title = 'THÊM BÀI VIẾT MỚI'
    bai_viet = None
    button = 'Thêm'
  form = BaiVietForm(instance=bai_viet)
  if request.POST:
    form = BaiVietForm(request.POST, instance=bai_viet)
    baiviet_update = form.save()
    if bai_viet:
      messages.success(request, f'Thông tin chỉnh sửa bài viết {baiviet_update.tieu_de} đã được lưu lại')
    else:
      messages.success(request, f'Bài viết {baiviet_update.tieu_de} đã được thêm thành công')
    return redirect('dsbaiviet')
  return render(request, 'baiviet.html', {'title': title, 'form': form, 'button': button})