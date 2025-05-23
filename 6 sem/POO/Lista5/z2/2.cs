public class CaesarStream : Stream
{
    private readonly Stream _innerStream;
    private readonly int _shift;

    public CaesarStream(Stream stream, int shift)
    {
        _innerStream = stream;
        _shift = shift;
    }

    public override void Write(byte[] buffer, int offset, int count)
    {
        byte[] encoded = new byte[count];
        for (int i = 0; i < count; i++)
        {
            encoded[i] = (byte)(buffer[offset + i] + _shift);
        }
        _innerStream.Write(encoded, 0, count);
    }

    public override int Read(byte[] buffer, int offset, int count)
    {
        int readBytes = _innerStream.Read(buffer, offset, count);
        for (int i = 0; i < readBytes; i++)
        {
            buffer[offset + i] = (byte)(buffer[offset + i] + _shift);
        }
        return readBytes;
    }

    public override bool CanRead => _innerStream.CanRead;
    public override bool CanSeek => false;
    public override bool CanWrite => _innerStream.CanWrite;
    public override long Length => _innerStream.Length;

    public override long Position { get => _innerStream.Position; set => _innerStream.Position = value; }

    public override void Flush() => _innerStream.Flush();
    public override long Seek(long offset, SeekOrigin origin) => throw new NotSupportedException();
    public override void SetLength(long value) => _innerStream.SetLength(value);
}
